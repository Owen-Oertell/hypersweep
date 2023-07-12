#!/bin/bash
#SBATCH -J job_group_learning_rate=0.001
#SBATCH -o stdout%j.log  # Name of stdout output file (%j expands to jobId)
#SBATCH -e stderr%j.err  # Name of stderr output file
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<email_address>
#SBATCH -N 1   # Total number of CPU nodes requested
#SBATCH -n 10  # Total number of CPU cores requrested
#SBATCH -t 96:00:00  # Run time (hh:mm:ss)
#SBATCH --mem=250G  # CPU Memory pool for all cores
#SBATCH --gres=gpu:a6000:2
#SBATCH --partition=<partition_name>
#SBATCH --get-user-env
conda activate .
python3 main.py --config.lr=0.001 