from oxDNA_analysis_tools.oxDNA_PDB import get_nucs_from_PDB, choose_reference_nucleotides, write_strand_to_PDB
from os import listdir

nucs = []
pdbfiles = [f for f in listdir() if '.pdb' in f]
print("To read:", pdbfiles)
for f in pdbfiles:
    nucs += get_nucs_from_PDB(f)

best = choose_reference_nucleotides(nucs)
for v in best.values():
    v.set_com([0, 0, 0])

for k, v in best.items():
    s = [v.to_pdb(True, 0)]
    with open('nucleotides/'+k+'.pdb', 'w+') as f:
        write_strand_to_PDB(s, "A", 1, f)