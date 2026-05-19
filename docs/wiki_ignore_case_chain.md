# Ignore case chain

The ignore_case_chain setting (default: **off**) controls whether the **chain** and **segi** selection operators are case sensitive. The default is to be case sensitive, so "chain A" is different from "chain a".

- New In PyMOL 1.8.2 (see ignore_case for previous versions)*

##  Example
The PDB structure **3tcx** has 28 chains, including "A" and "a".

 PyMOL>fetch 3tcx, async=0
 PyMOL>count_atoms chain A
  count_atoms: 641 atoms
 PyMOL>set ignore_case_chain, on
 PyMOL>count_atoms chain A
  count_atoms: 1282 atoms
