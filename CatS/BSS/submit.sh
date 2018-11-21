#!/usr/bin/env bash

if [ ! -f "$1" ];
then
    echo "Missing ligand pair file!"
    exit 1
fi

# Loop over all ligand pairs.
while read pair;
do
    # Extract the ligand numbers.
    lig0=$(echo "$pair" | awk '{print $1}')
    lig1=$(echo "$pair" | awk '{print $2}')

    # Print job info.
    echo "Submitting ligand pair: $lig0, $lig1"

    # Create the job name.
    name="${lig0}_${lig1}"

    # Create the Slurm submission script.
    cp template.slm submit.slm
    sed -i "s/NAME/${name}/g" submit.slm
    sed -i "s/LIG0/${lig0}/g" submit.slm
    sed -i "s/LIG1/${lig1}/g" submit.slm

    # Submit the job.
    sbatch submit.slm

    # Remove the redundant batch script.
    rm submit.slm

done < $1
