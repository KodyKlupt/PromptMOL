# Protect

- *protect** protects a set of atoms from tranformations performed using the editing features.  This is most useful when you are modifying an internal portion of a chain or cycle and do not wish to affect the rest of the molecule.

## USAGE
 protect (selection)

## PYMOL API
```python
cmd.protect(string selection)
```

##  Example
This example makes a very cool little, and fake, molecular movie.  Copy/paste this into PyMOL:

```python
load $PYMOL_PATH/test/dat/pept.pdb, obj

1. create the fake trajectory (of states)
for a in range(2,31): cmd.create("obj","obj",1,a)
1. remove the bond
unbond 5/C, 6/N
1. This protects everything but all atoms witing 4
1. Ang. of residue 5's carbon and residue 6's nitrogen.
protect not ((5/C or 6/N) extend 4)

1. do some quick sculpting
sculpt_activate obj, 30
sculpt_iterate obj, 30, 100
smooth obj, 30, 3

1. then program a bond-break/re-form movie
mset 1 x30 1 -30 30 x30 30 -1
mdo 45: unbond 5/C, 6/N, quiet=1
mdo 100: bond 5/C, 6/N, quiet=1

frame 100

as sticks
orient 5-6/N+CA+C
mplay
```
