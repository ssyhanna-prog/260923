#!/bin/bash
#SBATCH --job-name=h2-d2-hd-gibbs
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00

cd /home/acc-2026-28676/h2_d2_hd_gibbs
maestro-python calculate_raw_pyscf.py  # maestro: raw
