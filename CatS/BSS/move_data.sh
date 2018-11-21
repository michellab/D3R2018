#!/usr/bin/env bash

# Make the output directory.
mkdir -p "/mnt/shared/data/$1"

# Move out output files.
mv *.out "/mnt/shared/data/$1/"

# Move the output directories.
for i in $(ls -d */ | grep '^[0-9]');
do
    mv $i/* "/mnt/shared/data/$1/"
    rm -r $i
done
