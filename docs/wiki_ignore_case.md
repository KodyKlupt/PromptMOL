# Ignore case

The ignore_case setting (default: **on**, *except in PyMOL 1.8.0.0 - 1.8.0.4*) controls whether PyMOL does case sensitive matching of atomic identifiers and selection operators in the selection language. Most notably, it affects whether chain identifiers are matched case sensitive, which becomes relevant when using upper and lower case chain identifiers in a structure with more than 26 chains.

The default value was changed to **off** in PyMOL 1.8.0.0. However, due to undesired side effects, the **on** default was restored in 1.8.0.5.

The next PyMOL version (expect 1.8.2) will introduce a new ignore_case_chain setting to address the issue of mixed case chain identifiers.

See also: https://sourceforge.net/p/pymol/mailman/message/34815599/

##  Example
Load 1a00 which has chains A, B, C, D

 PyMOL>fetch 1a00, async=0

1) case insensitive selection language (default for PyMOL = 1.8.0.5)

 PyMOL>set ignore_case
  Setting: ignore_case set to on.
 PyMOL>count_atoms chain A
  count_atoms: 1164 atoms
 PyMOL>count_atoms chain a
  count_atoms: 1164 atoms

2) case sensitive selection language (default for PyMOL 1.8.0.0 - 1.8.0.4)

 PyMOL>set ignore_case, off
  Setting: ignore_case set to off.
 PyMOL>count_atoms chain A
  count_atoms: 1164 atoms
 PyMOL>count_atoms chain a
  count_atoms: 0 atoms

##  Best Practice for Scripting
When writing scripts or plugins, all selection expressions should be strict about case (e.g. "name CA" and not "name ca") to not depend on the users setting of ignore_case.
