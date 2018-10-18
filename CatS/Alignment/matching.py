import BioSimSpace as BSS
import glob

gc_3_ligs = glob.glob('../CatS_prep/GC3_data/ligands/*.pdb')
#gc_4_ligs = glob.glob('../CatS_prep/Docked_ligands/*.pdb')
gc_4_ligs = []
f = open('../CatS_initial_packet_to_participants/free_energies/missing.dat', 'r')
lines = f.readlines()
f.close()
for l in lines:
    gc_4_ligs.append('../CatS_prep/Docked_ligands/'+l.strip().split('_aligned.pdb')[0]+'.pdb')

best_match_list = []
match_pair_list = []
f = open('matching_missing.dat', 'w')
for gc4 in gc_4_ligs:
    best_match = 0
    match_pair = []
    gc4_mol = BSS.IO.readMolecules(gc4)
    for gc3 in gc_3_ligs:
        gc3_mol = BSS.IO.readMolecules(gc3)
        mapping = BSS.Align.matchAtoms(gc3_mol.getMolecules()[0], gc4_mol.getMolecules()[0])
        curr_map = len(mapping)
        print(curr_map)
        if best_match < curr_map:
            best_match = curr_map
            match_pair = [gc4,gc3]
            print ("Current best match is: %s,%s" %(gc4,gc3))
    best_match_list.append(best_match)
    match_pair_list.append(match_pair)
    f.write('%d, %s, %s\n' %(best_match_list[-1],match_pair_list[-1][0], match_pair_list[-1][1]))
f.close()
#f = open('matching_missing.dat', 'w')
#for i in range(len(best_match_list)):
#    f.write('%d, %s, %s\n' %(best_match_list[i],match_pair_list[i][0], match_pair_list[i][1]))
#f.close()

f = open('matching_missing.dat')
lines = f.readlines()
f.close()

for line in lines:
    a = line.strip().split(', ')
    out_name = a[1].split('/')[-1].split('.pdb')[0]+'_aligned.pdb'
    command = '/home/ppxasjsm/source_builds/kcombu/fkcombu -T %s -R %s -opdbT %s' %(a[1],a[2],out_name)
    os.system(command)
