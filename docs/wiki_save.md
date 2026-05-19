# Save

- *save** writes selected atoms to a file.

=Details=
- The file format is autodetected if the extension is .pdb, .pqr, .mol, .sdf, .pkl, .pkla, .mmd, .out, .dat, .mmod, .pmo, .pov, .png, .pse, .psw, .aln, .fasta, .obj, .mtl, .wrl, .idtf, .dae, or .mol2.
- If the file extension is ".pse" (PyMOL Session), the complete PyMOL state is always saved to the file (the selection and state parameters are thus ignored).
- CLUSTALW formatted alignments can be written by PyMOL as well. Once you perform an alignment like the following,
::
```python
align proteinA, proteinB, object=A_on_B
```

::the alignment can be written using:
::
```python
save A_aligned_with_B.aln, A_on_B
```

### USAGE
```python
save file [,(selection) [,state [,format]] ]
```

###  EXAMPLES
```python
1. save only the alpha carbons
save onlyCAs.pdb, n. CA

1. save my MD trajectory file to disk
save myTraj.pdb, myMDTrajectory, state=0

1. save a PyMOL session
save thisSession.pse
```

### PYMOL API
```python
cmd.save(filename[, selection[, state[, format]]])
```

### NOTES
- When saving a session file, then "state" has no effect.
- Default is state = -1, which saves only the current state.
- When state = 0, all states in the file are written. If you have more than one state, this produces a multi-state PDB file.

### SEE ALSO
Load, Get Model
