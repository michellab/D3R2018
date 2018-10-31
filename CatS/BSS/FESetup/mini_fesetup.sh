#!/bin/bash

fix=setup-
for i in CatS_178.in CatS_29.in CatS_191.in CatS_30.in CatS_29.in CatS_155.in CatS_153.in CatS_157.in;
do
	~/Software/FESetup1.2.1/FESetup64/bin/FESetup $fix$i > $i.out &
done
