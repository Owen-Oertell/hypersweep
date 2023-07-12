# hypersweep.py is a python script that does a hyperparameter sweep for a given command line function
from config import cfg
import os
import itertools

def runJob(main_name, parameters, job_name, job_group, slurm_parameters, conda_env):
    # create a slurm job
    job = open("sbatch.sh", "w")
    job.write("#!/bin/bash\n")
    job.write("#SBATCH -J " + job_group + "_" + job_name + "\n")
    for s in slurm_parameters:
        job.write(s + "\n")

    # add the conda environment
    job.write(conda_env + "\n")

    # add the command
    job.write(main_name + " ")
    for k,v in parameters.items():
        job.write(k + "=" + str(v) + " ")
    
    job.close()

    # submit the job
    os.system("sbatch sbatch.sh")
    os.remove("sbatch.sh")

def main():
    # get all the parameters to sweep over
    sweep_parameters = cfg.parameters_to_sweep
    set_parameters = cfg.set_parameters

    # get the command line names
    command_line_names = cfg.command_line_names

    # get the main command
    main_command = cfg.main_command

    # create cartesian produce over all parameters
    parameters = []
    for i in itertools.product(*sweep_parameters.values()):
        parameters.append(dict(zip(sweep_parameters.keys(), i)))

    for job in parameters:
        # add the set parameters
        for k,v in set_parameters.items():
            job[k] = v

        job_final = {}
        for k,v in job.items():
            job_final[command_line_names[k]] = v

        # create the job name
        job_name = ""
        for k,v in job.items():
            job_name += k + "=" + str(v) + "_"
        job_name = job_name[:-1]
    
        # run job
        runJob(main_command, job_final, job_name, cfg.job_group, cfg.slurm_parameters, cfg.conda_env)

if __name__ == "__main__":
    main()