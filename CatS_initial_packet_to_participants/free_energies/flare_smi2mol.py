from cresset import flare

project = flare.main_window().project

for l in project.ligands:
    f_name = l.title.split(':1')[0]
    l.minimize()
    l.write_file(f_name+'.mol2')
    
