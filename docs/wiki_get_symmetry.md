# Get Symmetry

- *get_symmetry** can be used to obtain the crystal and spacegroup parameters for a molecule or map object.

### USAGE
 get_symmetry object-name-or-selection

### DESCRIPTION
Returns a tuple containing the following 7 values:

- The unit cell lengths (a,b,c)
- The unit cell angles (alpha, beta, gamma)
- The space group name (e.g. "P 21 21 21")

### PYMOL API
```python
cmd.get_symmetry(string selection)
```

### See Also
- set_symmetry
- symmetry_copy
- Supercell
