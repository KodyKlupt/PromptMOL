# Fab

- *fab** builds peptide entities from sequence. The sequence must be specified in one-letter code. Several fragments will be created if the sequence contains spaces (chain breaks). To specify chain-id and residue number, an advanced syntax pattern like *chain/resi/* can be put before each sequence fragment.

Similar functionality is also provided by the graphical Builder in "Protein" mode.

- New in PyMOL version 1.2*

##  USAGE
 fab input [, name [, mode [, resi [, chain [, segi [, state [, dir [, hydro [, ss [, async ]]]]]]]]]]

##  ARGUMENTS
- input = string: Amino acid sequence in one-letter code

- name = string: name of object to create or modify {default: obj??}

- mode = string: Only supported mode is "peptide" {default: peptide}

- resi = integer: Residue number to start numbering from {default: 1}

- chain, segi = string: Chain id and segment id to assign

- state = integer: {default: -1}

- dir = 0/1: 0=append to N-terminus, 1=append to C-terminus {default: 1}

- hydro = 0/1: With or without hydrogens (BROKEN! Use auto_remove_hydrogens}

- ss = int: Secondary structure 1=alpha helix, 2=antiparallel beta, 3=parallel beta, 4=flat {default: 0}

##  EXAMPLE
The two examples produce the same result:

```python
1. use resi and chain attributes
fab KVRISAEL, myprot1, resi=10, chain=B, ss=2

1. use advanced syntax
fab B/10/ KVRISAEL, myprot2, ss=2
```
