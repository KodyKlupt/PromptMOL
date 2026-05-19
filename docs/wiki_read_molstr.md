# Read Molstr

- *read_molstr** reads an MDL MOL format file as a string

### PYMOL API ONLY
```python
cmd.read_molstr( string molstr, string name, int state=0, \
  int finish=1, int discrete=1 )
```

### NOTES
- **state** is a 1-based state index for the object, or 0 to append.

- **finish** is a flag (0 or 1) which can be set to zero to improve performance when loading large numbers of objects, but you must call **finish_object** when you are done.

- **discrete** is a flag (0 or 1) which tells PyMOL that there will be no overlapping atoms in the file being loaded.  **discrete** objects save memory but can not be edited.
