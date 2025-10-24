# oxDNA backmapping templates

This library generates the nucleotide fragments used by the oxDNA -> PDB converter for backmapping.

## PDB files
Representative PDB files of nice A-form RNA helices and B-form DNA helices were obtained from the PDB.
The requirement is that the library must contain at least one (and preferably more) of all common nucleotides,
including 5' and 3' ends (A, U, G, C, DA, DT, DG, DC, RA5, RU5, RG5, RC5, DA5, DU5, DG5, DC5, RA3, RU3, RG3, RC3, DA3, DU3, DG3, DC3).

Because most simple duplexes in the PDB database include some sort of modified nucleotide, this sampling will generate structures for a couple modified nucleotides such as RNA pseudouridine and DNA 5HC. They're kept in the output because why not?

All structures were cleaned of ions, waters and non-nucleic acids and their residue and atom names modified to match the [AMBER/CHARMM naming conventions](https://userguide.mdanalysis.org/stable/standard_selections.html#nucleic-acids).  Note that most DNA PDB files do not have correctly named terminal residues and must be manually updated before being added here.

RNA structures were optimized with [QRNA](https://github.com/sunandanmukherjee/QRNAS).

## Paragon selection
To create a library of nucleic acid fragments to use with backmapping, `get_paragons.py` loads all PDB files in the current directory and selects the "best" example of each residue based on the criteria given in [choose_reference_nucleotides](https://lorenzo-rovigatti.github.io/oxDNA/oat/api.html#oxdna-to-pdb). Currently, this function just picks nucleotides based on how flat their bases are, but this could be updated in the future to also include oxDNA-like placement of the backbone/base sites.

## Contributing
If you want to expand the template library or improve the paragon selection function, pull requests are welcome here or to the main [oxDNA](https://github.com/lorenzo-rovigatti/oxDNA) repository!