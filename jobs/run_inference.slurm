#!/bin/bash
#SBATCH -J inference               # job name
#SBATCH -o logs/inference.%j.out   # stdout (the %j is the job ID)
#SBATCH -e logs/inference.%j.err   # stderr
#SBATCH -p gh                      # queue: gh (GPU); use gh-dev for short pilot jobs
#SBATCH -N 1                       # nodes
#SBATCH -n 1                       # tasks
#SBATCH -t 04:00:00                # wall time (hh:mm:ss) — raise for 70B-class sweeps
#SBATCH -A TRA25001                # workshop allocation; change to your own after the program

# Load modules and activate your environment
module load python3
source .venv/bin/activate

# PILOT FIRST on the gh-dev queue:
#   python scripts/run_inference.py --limit 10 --models meta-llama/Meta-Llama-3-8B-Instruct
# Then the full sweep (reads data/processed/prompts.csv, writes data/processed/responses.csv):
python scripts/run_inference.py --reps 3

# Scoring (judge model) can run as a second job, or append here:
#   python scripts/evaluate.py
