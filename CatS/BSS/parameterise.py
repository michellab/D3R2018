import BioSimSpace as BSS

import re
import sys

# Read the list of ligands.
ligands = []
with open("ligands.txt", "r") as file:
    for line in file:
        ligands.append(line.rstrip())

# Get the ligand index.
idx = int(sys.argv[1])

# Extract the ligand name.
lig_name = re.search("(CatS_\d+).pdb", ligands[idx]).groups()[0]

# Create the prefix of the output files.
output = "ligands_aligned/parameterised/" + lig_name

# Load the ligand.
lig = BSS.IO.readMolecules("ligands_aligned/" + ligands[idx]).getMolecules()[0]

# Parameterise the ligand with GAFF2.
lig = BSS.Parameters.gaff2(lig).getMolecule()

# Save to AMBER format.
BSS.IO.saveMolecules(output, lig, ["rst7", "prm7"])
