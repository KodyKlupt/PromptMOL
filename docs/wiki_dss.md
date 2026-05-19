# Dss

- *dss** *d*efines *s*econdary *s*tructure based on backbone geometry and hydrogen bonding patterns.

With PyMOL, heavy emphasis is placed on cartoon aesthetics, and so both hydrogen bonding patterns and backbone geometry are used in the assignment process.  Depending upon the local context, helix and strand assignments are made based on geometry, hydrogen bonding, or both.

This command will generate results which differ slightly from DSSP and other programs.  Most deviations occur in borderline or transition regions.  Generally speaking, PyMOL is more strict, thus assigning fewer helix/sheet residues, except for partially distorted helices, which PyMOL tends to tolerate.

WARNING: This algorithm has not yet been rigorously validated.

### USAGE
 dss [selection [, state]]

###  ARGUMENTS
- selection = string: atom selection {default: (all)}
- state = integer: state-index if positive number or any of these:
- * state = 0: consensus over all states {default}
- * state = -1: current state
- * state = -2: consensus over effective object states (implemented?)
- * state = -3: no consensus, residue gets assignment from earliest state that is not 'L'
- * state = -4: consensus over first and last state

### EXAMPLES
```python
1. determine secondary structures in
1. all loaded objects in PyMOL
dss
```

### NOTES
If you dislike one or more of the assignments made by dss, you can use the alter command to make changes (followed by "rebuild").
For example:

```python
1. set residues 123-125 as being loops
alter 123-125/, ss='L'

1. set the secondary structure of selection (pk1) to beta sheet
alter pk1, ss='S'

1. set residue 90 to be alpha-helical
alter 90/, ss='H'

1. update the scene in PyMOL to reflect the changes.
rebuild
```

#### Secondary Structure Determination
As is typical with PyMOL, the secondary structure assignment engine is ad hoc and empirically tuned to produce desirable aesthetics.  Though there are some phi/psi's that are clearly helix/sheet and others that are clearly not, there are certain regions of phi/psi space were the assignment is subjective or arbitrary.  In my experience, algorithms based on strict definitions tend to operate poorly in such regions, and so PyMOL's algorithm is "fuzzy" in that there is a grey area where residues may be accepted or rejected as helix/sheet depending upon the surrounding context.

There aren't any hard & fast definitions.  But you are welcome to check out the collection of settings beginning with "ss_helix" and "ss_strand", noting that the include and exclude settings are deviations around the target in degrees.  If you think PyMOL is incorrectly assigning secondary structure, then you might try varying these.
