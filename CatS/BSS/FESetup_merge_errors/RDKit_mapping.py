from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw
from rdkit.Chem import rdFMCS
import sys

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('Usage: python RDKit_mapping.py file1.pdb file2.pdb outputfilename')
	else:
		print('Attempting mapping %s and %s and writing mapping to %s' %(sys.argv[1], sys.argv[2], sys.argv[3]))


CatS1 = Chem.MolFromPDBFile(sys.argv[1])
CatS2 = Chem.MolFromPDBFile(sys.argv[2])
outfile = sys.argv[3]
img = Draw.MolsToGridImage([CatS1,CatS2],subImgSize=(300,300))
img.save('molecules.png')
mcs = rdFMCS.FindMCS([CatS1,CatS2], completeRingsOnly=True,timeout=12000)
result = rdFMCS.MCSResult
mcsp = Chem.MolFromSmarts(mcs.smartsString)
match1 = CatS1.GetSubstructMatch(mcsp)
match2 = CatS2.GetSubstructMatch(mcsp)
mapping = dict(zip(match1, match2))
print("mapping has a length of %d " %len(mapping))

print("Writing mapping to file: ")
f = open(outfile, 'w')
for k,v in mapping.items():
    f.write('%d %d\n' %(k,v))
f.close()

print("Displaying core structure and smarts string of core structure")
