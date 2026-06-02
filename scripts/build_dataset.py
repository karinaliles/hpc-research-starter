"""Assemble the unified evaluation prompt set in data/processed/prompts.csv.

[laptop / login node]  Phase 1 of the methodology.

Unions the prompt sources into one table that matches the Table 1 schema in
framework/data-spec.md, validates it, and reports per-domain coverage:
  - framework/community-prompts.csv     (authored seed prompts)
  - framework/bbq-seeded-prompts.csv    (real BBQ items, benchmark-linked)
  - framework/community-contributed.csv (optional; produced during community validation)

Run:  python scripts/build_dataset.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK = ROOT / "framework"
OUT = ROOT / "data" / "processed" / "prompts.csv"

# Unified Table 1 schema (see framework/data-spec.md)
REQUIRED = ["prompt_id", "prompt_text", "domain", "primary_dimension", "high_stakes"]
PROVENANCE = ["source", "community_validated"]
BBQ_FIELDS = ["bbq_example_id", "bbq_category", "bbq_context_condition", "unbiased_answer"]

SOURCES = [
    (FRAMEWORK / "community-prompts.csv", "authored"),
    (FRAMEWORK / "bbq-seeded-prompts.csv", "bbq-seeded"),
    (FRAMEWORK / "community-contributed.csv", "community-contributed"),  # optional
]


def load_source(path: Path, default_source: str) -> pd.DataFrame:
    """Load one prompt CSV, stamping provenance defaults if absent."""
    if not path.exists():
        print(f"  (skip) {path.name} not found")
        return pd.DataFrame()
    df = pd.read_csv(path)
    if "source" not in df.columns:
        df["source"] = default_source
    if "community_validated" not in df.columns:
        # authored/seeded prompts are unvalidated until the community signs off
        df["community_validated"] = "no"
    print(f"  loaded {len(df):>3} rows from {path.name}")
    return df


def validate(df: pd.DataFrame) -> None:
    """Fail loudly on schema or integrity problems."""
    missing = [c for c in REQUIRED + PROVENANCE if c not in df.columns]
    if missing:
        sys.exit(f"ERROR: missing required columns: {missing}")
    dupes = df["prompt_id"][df["prompt_id"].duplicated()].tolist()
    if dupes:
        sys.exit(f"ERROR: duplicate prompt_id values: {dupes}")
    bad_dim = set(df["primary_dimension"]) - {"effectiveness", "equity", "trustworthiness"}
    if bad_dim:
        sys.exit(f"ERROR: unexpected primary_dimension values: {bad_dim}")
    blank = df["prompt_text"].isna() | (df["prompt_text"].str.strip() == "")
    if blank.any():
        sys.exit(f"ERROR: {blank.sum()} rows have empty prompt_text")


def main() -> None:
    print("Assembling prompt set...")
    frames = [load_source(p, s) for p, s in SOURCES]
    df = pd.concat([f for f in frames if not f.empty], ignore_index=True)

    # keep all known columns; fill BBQ fields with NA for non-seeded rows
    for col in BBQ_FIELDS:
        if col not in df.columns:
            df[col] = pd.NA
    df = df[REQUIRED + PROVENANCE + BBQ_FIELDS]

    validate(df)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    print(f"\nWrote {len(df)} prompts -> {OUT.relative_to(ROOT)}")
    print("\nCoverage by domain:")
    print(df["domain"].value_counts().to_string())
    print(f"\nValidated by community: "
          f"{(df['community_validated'] == 'yes').sum()} / {len(df)}")
    # TODO (after community validation): expect ~150 rows, most community_validated == 'yes'


if __name__ == "__main__":
    main()
