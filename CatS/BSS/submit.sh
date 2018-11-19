#!/usr/bin/env bash

# Loop over all ligand pairs.
while read pair;
do
    # Extract the ligand numbers.
    lig0=$(echo "$pair" | awk '{print $1}')
    lig1=$(echo "$pair" | awk '{print $2}')

    # Print job info.
    echo "Submitting ligand pair: $lig0 --> $lig1"

    # Create the job name.
    name="CatS_${lig0}_${lig1}"

    # Create the Slurm submission script.
    cp template.slm submit.slm
    sed -i "s/NAME/${name}/g" submit.slm
    sed -i "s/LIG0/${lig0}/g" submit.slm
    sed -i "s/LIG1/${lig1}/g" submit.slm

    # Make GPU 0 the first visible device.
    export CUDA_VISIBLE_DEVICES=0,1

    # Submit the job.
    sbatch submit.slm

    # Now do the reverse mapping.

    # Print job info.
    echo "Submitting ligand pair: $lig1 --> $lig0"

    # Create the job name.
    name="CatS_${lig1}_${lig0}"

    # Create the Slurm submission script.
    cp template.slm submit.slm
    sed -i "s/NAME/${name}/g" submit.slm
    sed -i "s/LIG0/${lig1}/g" submit.slm
    sed -i "s/LIG1/${lig0}/g" submit.slm

    # Make GPU 1 the first visible device.
    export CUDA_VISIBLE_DEVICES=1,0

    # Submit the job.
    sbatch submit.slm

done < ligand_pairs.txt
