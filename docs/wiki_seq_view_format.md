# Seq view format

###  OVERVIEW
The **seq_view_format** setting controls how PyMOL displays the sequence viewer.  (To turn on the sequence viewer, type, **set seq_view, on**.)  The available formats are currently:

- 0 = Display residues as single letter amino acid names
- 1 = Display residues as triple letter amino acid names
- 2 = Displays all atoms in each residue based on their atom name
- 3 = Displays each peptide chain

### SYNTAX
```python
1. usage
set seq_view_format, number

1. default
set seq_view_format, 0

1. triple letter amino acids
set seq_view_format, 1
```

### SEE ALSO
Seq_view
