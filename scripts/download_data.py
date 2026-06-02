"""Download the open model weights and the BBQ benchmark onto Vista $SCRATCH.

[Vista]  Phase 2 of the methodology.  Large files stay on $SCRATCH, never in Git.

Prereqs:  pip install huggingface_hub ;  huggingface-cli login   (for gated models)

Run:  python scripts/download_data.py
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

# Models to evaluate. TODO: confirm the final list with the compute plan in
# templates/methodology.md. Pin sizes deliberately — model size is the main HPC driver.
MODELS = [
    "meta-llama/Meta-Llama-3-8B-Instruct",      # small contrast model
    # "meta-llama/Meta-Llama-3-70B-Instruct",   # TODO: enable 70B-class for the real run
    # "mistralai/Mixtral-8x7B-Instruct-v0.1",
    # "Qwen/Qwen2-72B-Instruct",
    # "google/gemma-2-27b-it",
]

# The judge model used later in evaluate.py (download it here too).
JUDGE_MODEL = "meta-llama/Meta-Llama-3-70B-Instruct"  # TODO: confirm judge choice

BBQ_REPO = "https://github.com/nyu-mll/BBQ.git"  # CC-BY 4.0


def scratch() -> Path:
    """Resolve $SCRATCH (Vista); fall back to data/raw/ locally for dry runs."""
    base = os.environ.get("SCRATCH")
    root = Path(base) if base else Path(__file__).resolve().parents[1] / "data" / "raw"
    return root


def download_models(dest: Path) -> None:
    from huggingface_hub import snapshot_download  # imported lazily so --help works without it

    for model_id in [*MODELS, JUDGE_MODEL]:
        target = dest / "models" / model_id.replace("/", "__")
        print(f"Downloading {model_id} -> {target}")
        # TODO: set allow_patterns to skip unneeded files; handle gated-model auth errors
        snapshot_download(repo_id=model_id, local_dir=str(target), local_dir_use_symlinks=False)


def download_bbq(dest: Path) -> None:
    target = dest / "BBQ"
    if target.exists():
        print(f"BBQ already present at {target}")
        return
    print(f"Cloning BBQ -> {target}")
    subprocess.run(["git", "clone", "--depth", "1", BBQ_REPO, str(target)], check=True)


def main() -> None:
    dest = scratch()
    dest.mkdir(parents=True, exist_ok=True)
    print(f"Download destination: {dest}")
    download_bbq(dest)
    download_models(dest)
    print("Done. Model weights + BBQ are on $SCRATCH.")


if __name__ == "__main__":
    main()
