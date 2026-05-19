# Cif keepinmemory

The cif_keepinmemory setting is an experimental feature. When loading a CIF file with **cif_keepinmemory**=on, then the parsed file is kept in memory and made accessible like a dictionary from the Python API.

- New in PyMOL 1.7.8*

##  Examples
```python
import pymol

pymol.cmd.set("cif_keepinmemory")
pymol.cmd.fetch("1ubq", type="cif")

citation_titles = pymol.querying.cif_get_array("1ubq", "_citation.title")

import pprint
pprint.pprint(citation_titles)
```

Output:

 ['Structure of ubiquitin refined at 1.8 A resolution.',
  'Comparison of the Three-Dimensional Structures of Human, Yeast, and Oat Ubiquitin',
  'Three-Dimensional Structure of Ubiquitin at 2.8 Angstroms Resolution',
  'Crystallization and Preliminary X-Ray Investigation of Ubiquitin, a Non-Histone Chromosomal Protein',
  'Molecular Conservation of 74 Amino Acid Sequence of Ubiquitin between Cattle and Man']
