#!/bin/bash -login
#SBATCH --nodes=1
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=14
#SBATCH --job-name=NAME
#SBATCH --output=NAME.out
#SBATCH --time=100:00:00
#SBATCH --mem=40G

# Disable Sire analytics.
export SIRE_DONT_PHONEHOME=1
export SIRE_SILENT_PHONEHOME=1

# Make sure nvcc is in the path.
export PATH=/usr/local/cuda-9.0/bin:$PATH

# Set path to local AmberTools installation.
export AMBERHOME=/mnt/shared/software/amber18

# Source the GROMACS shell rc, making sure mount point exists.
while [ ! -f /mnt/shared/software/gromacs/bin/GMXRC ]; do
    sleep 1s
done
source /mnt/shared/software/gromacs/bin/GMXRC

# Set the OpenMM plugin directory.
export OPENMM_PLUGIN_DIR=/mnt/shared/software/sire.app/lib/plugins

# Make a unique directory for this job and move to it.
mkdir $SLURM_SUBMIT_DIR/$SLURM_JOB_ID
cd $SLURM_SUBMIT_DIR/$SLURM_JOB_ID

export JOB_DIR=$SLURM_SUBMIT_DIR

# Run the script using the BioSimSpace python interpreter.

# Make sure GPU ID 0 is first.
export CUDA_VISIBLE_DEVICES=0,1

# Forwards.
time /mnt/shared/software/sire.app/bin/sire_python --ppn=1 $JOB_DIR/binding_freenrg.py LIG0 LIG1 &

# Make sure GPU ID 1 is first.
export CUDA_VISIBLE_DEVICES=1,0

# Backwards.
time /mnt/shared/software/sire.app/bin/sire_python --ppn=1 $JOB_DIR/binding_freenrg.py LIG1 LIG0
wait
