#!/usr/bin/env bash

# Disable Sire analytics.
export SIRE_DONT_PHONEHOME=1
export SIRE_SILENT_PHONEHOME=1

# Create the name of the analysis command.
cmd="/mnt/shared/software/sire.app/bin/analyse_freenrg mbar -i "

# Loop over all of the job directories.
for job in $(ls -d */ | grep '^[0-9]');
do
    # Loop over the forward and backward ligand mappings.
    for pair in $(ls $job);
    do
        # Create the directory name.
        dir="$job$pair"

        # Get the last gradient iteration at lambda = 1.0
        # in order to see if the simulation has completed.

        # Generate the file name.
        filename="$dir/free/lambda_1.0/gradients.dat"

        if [ -f "$filename" ];
        then
            step=$(tail -n 1 $dir/free/lambda_1.0/gradients.dat | awk '{printf "%d", $1}')
        else
            step=0
        fi

        if [ $step -eq 50 ];
        then
            echo "Running free energy analysis for ligand pair: $pair"

            $cmd $dir/bound/*/simfile.dat -o ${pair}_mbar_bound.txt > /dev/null 2>&1
            $cmd $dir/free/*/simfile.dat -o ${pair}_mbar_free.txt > /dev/null 2>&1
        fi
    done
done
