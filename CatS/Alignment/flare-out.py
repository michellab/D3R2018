from cresset import flare

project = flare.main_window().project
pdb_dic = {}
pdb_dic['znpb'] = '5QC5'
pdb_dic['yquj'] = '5QCA'
pdb_dic['wcgq'] = '5QC3'
pdb_dic['ttlc'] = '5QBX'
pdb_dic['mekm'] = '5QC6'
pdb_dic['haan'] = '5QC4'

prot_dic = {}
prot_dic['haan-CatS_chainA-aligned_P']=0
prot_dic['znpb-CatS_chainA-aligned']=1
prot_dic['yquj-CatS_chainA-aligned']=2
prot_dic['wcgq-CatS_chainA-aligned']=3
prot_dic['ttlc-CatS_chainA-aligned']=4
prot_dic['mekm-CatS_chainA-aligned']=5

for l in project.ligands:
    if l.title.endswith('_score'):
        #
        raw_name = l.properties['Protein'].value
        docked_protein = raw_name.split('-')[0]
        print (docked_protein)
        print (pdb_dic[docked_protein])
        p = project.proteins[prot_dic[raw_name]]
        name = '/home/ppxasjsm/Projects/git/D3R2018/CatS/submission/score/'+pdb_dic[docked_protein]+'-'+l.title.strip('_score')+'.sdf'
        print(name)
        l.write_file(name)
        p_name =  '/home/ppxasjsm/Projects/git/D3R2018/CatS/submission/score/'+pdb_dic[docked_protein]+'-'+l.title.strip('_score')+'.pdb'
        print(p_name)
        p.write_file(p_name)
        #print(score)
        #f.write('%s,%f\n' %(name,score))
