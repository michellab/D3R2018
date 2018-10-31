#!/bin/bash

for i in *.in;
do
	~/Software/FESetup1.2.1/FESetup64/bin/FESetup $i > $i.out &
done
