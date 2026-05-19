# Edit

- *edit** picks an atom or bond for editing.

### USAGE
 edit (selection) [ ,(selection) ]

### PYMOL API
```python
cmd.edit( string selection  [ ,string selection ] )
```

### NOTES
If only one selection is provided, an atom is picked.
If two selections are provided, the bond between them
is picked (if one exists).

### SEE ALSO
unpick, remove_picked, cycle_valence, torsion
