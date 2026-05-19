# H Add

h_add uses a primitive algorithm to add hydrogens onto a molecule.

= Usage and Algorithm Notes =
PyMOL fills missing valences but does no optimization of hydroxyl rotamers.  Also, many crystal structures have bogus or arbitrary ASN/GLN/HIS orientations.  Getting the proper amide rotamers and imidazole tautomers & protonation states assigned is a nontrivial computational chemistry project involving electrostatic potential calculations and a combinatorial search.  There's also the issue of solvent & counter-ions present in systems like aspartyl proteases with adjacent carboxylates .

##  Accessing Through GUI
[A]->hydrogens->add

##  Syntax
```python
1. normal usage
h_add (selection)

1. API usage
cmd.h_add( string selection="(all)" )
```

see also H_Fill
