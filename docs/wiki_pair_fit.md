# Pair fit

Pair_Fit fits a set of atom pairs between two models.  Each atom in each pair must be specified individually, which can be tedious to enter manually.  Script files are recommended when using this command.

### USAGE
```python
pair_fit (selection), (selection), [ (selection), (selection) [ ...] ]
```

### EXAMPLES
```python
1. superimpose protA residues 10-25 and 33-46 to protB residues 22-37 and 41-54:
pair_fit protA///10-25+33-46/CA, protB///22-37+41-54/CA
1. superimpose ligA atoms C1, C2, and C3 to ligB atoms C8, C4, and C10, respectively:
pair_fit ligA////C1, ligB////C8, ligA////C2, ligB////C4, ligA////C3, ligB////C10
```

### NOTES
So long as the atoms are stored in PyMOL with the same order internally, you can provide just two selections.  Otherwise, you may need to specify each pair of atoms separately, two by two, as additional arguments to pair_fit.

Script files are usually recommended when using this command.

### USER EXAMPLES/COMMENTS
An description of selection caveats for these commands may be found at Rms.

### SEE ALSO
Fit, Rms, Rms_Cur, Intra_Fit, Intra_Rms, Intra_Rms_Cur
