# Read Pdbstr

- *read_pdbstr** in an API-only function which reads a pdb file from a Python string.  This feature can be used to load or update structures into PyMOL without involving any temporary files.

### PYMOL API ONLY
```python
cmd.read_pdbstr( string pdb-content, string object name
   [ ,int state [ ,int finish [ ,int discrete ] ] ] )
```

### NOTES
- *state** is a 1-based state index for the object.

- *finish** is a flag (0 or 1) which can be set to zero to improve performance when loading large numbers of objects, but you must call "finish_object" when you are done.

- *discrete** is a flag (0 or 1) which tells PyMOL that there will be no overlapping atoms in the PDB files being loaded. **discrete** objects save memory but can not be edited.
