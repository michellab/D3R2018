#!/usr/bin/env bash

# Move out output files.
mv *.out /mnt/shared/data/finished

# Move the output directories.
for i in $(ls -d */ | grep '^[0-9]');
do
    mv $i/* /mnt/shared/data/finished/;
    rm -r $i
done
