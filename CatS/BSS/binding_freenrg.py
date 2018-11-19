import BioSimSpace as BSS

# Load the protein and crystal waters.
protein_water = BSS.IO.readMolecules("protein/protein_water.pdb")

# Extract the waters.
waters = protein_water.getWaterMolecules()

# Parameterise the protein.
protein = BSS.Parameters.ff14SB(protein_water.getMolecules()[0]).getMolecule()

# Load the parameterised ligands.
lig0 = BSS.IO.readMolecules(BSS.IO.glob("ligands_aligned/parametrised/CatS_155.*")).getMolecules()[0]
lig1 = BSS.IO.readMolecules(BSS.IO.glob("ligands_aligned/parametrised/CatS_157.*")).getMolecules()[0]

# Find the best mapping of atoms between the ligands.
mapping = BSS.Align.matchAtoms(lig0, lig1)

# Align lig0 to lig1 based on the mapping.
lig0 = BSS.Align.rmsdAlign(lig0, lig1, mapping)

# Merged the two ligands based on the mapping.
merged = BSS.Align.merge(lig0, lig1, mapping)

# Create the composite system.
system = merged + protein + waters

# Solvate in a 60 angstrom box of TIP3P water.
solvated = BSS.Solvent.tip3p(molecule=system, box=3*[60*BSS.Units.Length.angstrom])

# Initialise the binding free energy object.
freenrg = BSS.FreeEnergy.Binding(solvated,
                                 BSS.Protocol.FreeEnergy(),
                                 work_dir="CatS_155_157")

# Run the simulation.
#freenrg.run()
