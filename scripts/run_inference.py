"""Generate model responses to every prompt and write data/processed/responses.csv.

[Vista, GPU]  Phase 3 of the methodology.  This is the main compute step.
Run on Vista via jobs/run_inference.slurm — NOT on your laptop.

For each (prompt x model x repetition) it generates one response with a FIXED seed and
LOGGED sampling settings, so the run is reproducible. Output schema = Table 2 in
framework/data-spec.md.

PILOT FIRST: pass --limit 10 --models <one-model> to smoke-test before the full sweep.

Run:  python scripts/run_inference.py [--limit N] [--reps 3]
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "data" / "processed" / "prompts.csv"
OUT = ROOT / "data" / "processed" / "responses.csv"

# TODO: keep in sync with scripts/download_data.py MODELS
MODELS = ["meta-llama/Meta-Llama-3-8B-Instruct"]

# Reproducibility knobs — log these with every row.
SAMPLING = {"temperature": 0.7, "top_p": 0.9, "max_tokens": 512}
BASE_SEED = 1234  # per-repetition seed = BASE_SEED + repetition_index


def scratch_model_path(model_id: str) -> Path:
    base = os.environ.get("SCRATCH")
    root = Path(base) if base else ROOT / "data" / "raw"
    return root / "models" / model_id.replace("/", "__")


def load_model(model_id: str):
    """Load a model for batched generation. Implemented with vLLM on Vista."""
    # from vllm import LLM
    # return LLM(model=str(scratch_model_path(model_id)), dtype="bfloat16",
    #            tensor_parallel_size=int(os.environ.get("GPUS_PER_NODE", "1")))
    raise NotImplementedError(
        "Vista step: load the model with vLLM (see commented template above). "
        "Pilot with --limit 10 on one model before scaling."
    )


def generate(llm, prompts: list[str], seed: int) -> list[str]:
    """Return one response per prompt. Implemented with vLLM SamplingParams on Vista."""
    # from vllm import SamplingParams
    # params = SamplingParams(seed=seed, **SAMPLING)
    # outs = llm.generate(prompts, params)
    # return [o.outputs[0].text for o in outs]
    raise NotImplementedError("Vista step: batch-generate with vLLM SamplingParams.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="cap prompts (pilot runs)")
    ap.add_argument("--reps", type=int, default=3, help="repetitions per prompt")
    ap.add_argument("--models", nargs="*", default=MODELS)
    args = ap.parse_args()

    df = pd.read_csv(PROMPTS)
    if args.limit:
        df = df.head(args.limit)
    print(f"{len(df)} prompts x {len(args.models)} models x {args.reps} reps "
          f"= {len(df) * len(args.models) * args.reps} generations")

    rows = []
    for model_id in args.models:
        llm = load_model(model_id)
        for rep in range(args.reps):
            seed = BASE_SEED + rep
            texts = generate(llm, df["prompt_text"].tolist(), seed)
            for (_, p), text in zip(df.iterrows(), texts):
                rows.append({
                    "prompt_id": p["prompt_id"],
                    "model_id": model_id,
                    "repetition": rep,
                    "response_text": text,
                    "sampling_settings": str(SAMPLING),
                    "seed": seed,
                    "refused": _looks_refused(text),
                    "truncated": _looks_truncated(text),
                })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"Wrote {len(rows)} responses -> {OUT.relative_to(ROOT)}")


def _looks_refused(text: str) -> bool:
    # TODO: refine refusal detection (e.g., "I can't help with that")
    return isinstance(text, str) and text.strip() == ""


def _looks_truncated(text: str) -> bool:
    # TODO: flag responses cut off at max_tokens
    return False


if __name__ == "__main__":
    main()
