from ml_collections import config_dict

# define the config
cfg = config_dict.ConfigDict()

# slurm parameters
cfg.slurm_parameters = [ # don't include the job name. that will be added automatically
    "#SBATCH -o stdout%j.log  # Name of stdout output file (%j expands to jobId)",
    "#SBATCH -e stderr%j.err  # Name of stderr output file",
    "#SBATCH --mail-type=ALL",
    "#SBATCH --mail-user=<email_address>",
    "#SBATCH -N 1   # Total number of CPU nodes requested",
    "#SBATCH -n 10  # Total number of CPU cores requrested",
    "#SBATCH -t 96:00:00  # Run time (hh:mm:ss)",
    "#SBATCH --mem=250G  # CPU Memory pool for all cores",
    "#SBATCH --gres=gpu:a6000:2",
    "#SBATCH --partition=<partition_name>",
    "#SBATCH --get-user-env"
]


# define the hyperparameters
cfg.main_command = "python3 main.py"

# define the slurm conda environment
cfg.conda_env = "conda activate ."

# group name
cfg.job_group = "job_group"

# define how to add them to the command line
# make sure to specify run_name and group_name for wandb
cfg.command_line_names = {
    "learning_rate": "--config.lr",

}

# set of parameters that we want to sweep. Provide a list of values that we want to sweep over
cfg.parameters_to_sweep = {
    "learning_rate" : [0.1, 0.01, 0.001],
}

# set of parameters that we want to hold fixed (not swept over)
cfg.set_parameters = {

}
