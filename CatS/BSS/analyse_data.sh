#!/usr/bin/env bash

# Disable Sire analytics.
export SIRE_DONT_PHONEHOME=1
export SIRE_SILENT_PHONEHOME=1

# Create the name of the analysis command.
cmd="/mnt/shared/software/sire.app/bin/analyse_freenrg mbar --subsampling --overlap --percent 90 -i "

# Remove old free energy data.
if [ -f free_energies.txt ];
then
    rm free_energies.txt
fi

# Print free energy file header.
printf "# %5s %5s %12s %12s %12s %12s %12s %12s\n" lig0 lig1 pmf_bound error pmf_free error delta error > free_energies.txt

# Loop over all of the job directories.
for job in $(ls -d */ | grep '^[0-9]');
do
    # Loop over the forward and backward ligand mappings.
    for pair in $(ls $job);
    do
        # Extract the ligand names.
        lig0=$(echo $pair | awk -F '_' '{print $2}')
        lig1=$(echo $pair | awk -F '_' '{print $3}')

        # Create the directory name.
        dir="$job$pair"

        # Get the last gradient iteration at lambda = 1.0
        # in order to see if the simulation has completed.

        # Generate the file name.
        filename="$dir/free/lambda_1.0000/gradients.dat"

        if [ -f "$filename" ];
        then
            step=$(tail -n 1 $filename | awk '{printf "%d", $1}')
        else
            step=0
        fi

        # Only process if the data set is complete.
        if [ $step -eq 200 ];
        then
            echo "Running free energy analysis for ligand pair: $pair"

            # Don't re-run analysis if already done.
            if [ ! -f ${dir}_mbar_bound.txt ];
            then
                $cmd $dir/bound/*/simfile.dat -o ${dir}_mbar_bound.txt > /dev/null 2>&1
            fi

            # Don't re-run analysis if already done.
            if [ ! -f ${dir}_mbar_free.txt ];
            then
                $cmd $dir/free/*/simfile.dat -o ${dir}_mbar_free.txt > /dev/null 2>&1
            fi

            # Extract bound and free leg free energies.
            pmf_bound=$(awk '/MBAR free/{getline; gsub(",", "", $0); print $1, $2}' ${dir}_mbar_bound.txt)
            pmf_free=$(awk '/MBAR free/{getline; gsub(",", "", $0); print $1, $2}' ${dir}_mbar_free.txt)

            # Only proceed if there is valid free energy data.
            if [ "$pmf_bound" != "" ] && [ "$pmf_free" != "" ];
            then
                # Extract the PMF and the associated error for each leg.
                bound_pmf=$(echo $pmf_bound | awk '{print $1'})
                bound_err=$(echo $pmf_bound | awk '{print $2'})
                free_pmf=$(echo $pmf_free | awk '{print $1'})
                free_err=$(echo $pmf_free | awk '{print $2'})

                # Print the results to file.
                printf "  %5s %5s %12.4f %12.4f %12.4f %12.4f\n" $lig0 $lig1 $bound_pmf $bound_err $free_pmf $free_err >> free_energies.txt
            fi
        fi
    done
done

# Work out the free energy difference and append to the file.
awk '{if (NR == 1) {print $0} else {printf("%s %12.4f %12.4f\n", $0, $3-$5, sqrt(($4*$4) + ($6*$6)))}}' free_energies.txt > tmp.txt
mv tmp.txt free_energies.txt

# Creat CSV file for network analysis code.
awk 'NR>1{printf "CatS_%s,CatS_%s,%5.4f,%5.4f\n", $1,$2,$7,$8}' free_energies.txt > free_energies.csv
