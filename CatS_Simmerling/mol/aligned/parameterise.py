import BioSimSpace as BSS

import re
import sys

# Read the list of ligands.
ligands = []
with open("ligands.txt", "r") as file:
    for line in file:
        ligands.append(line.rstrip())

print(ligands)
# Get the ligand index.
idx = int(sys.argv[1])
print(ligands[idx])
# Extract the ligand name.
lig_name = "CatS_"+ligands[idx]

# Create the prefix of the output files.
output = "parameterised/" + lig_name

# Load the ligand.
lig = BSS.IO.readMolecules(lig_name+'.mol2').getMolecules()[0]

# Parameterise the ligand with GAFF2.
lig = BSS.Parameters.gaff2(lig, work_dir='tmp_'+str(idx)).getMolecule()

# Save to AMBER format.
BSS.IO.saveMolecules(output, lig, ["rst7", "prm7"])
