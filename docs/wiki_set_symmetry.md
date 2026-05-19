# Set Symmetry

- *set_symmetry** can be used to define or redefine the crystal and spacegroup parameters for a molecule or map object.

### USAGE
 set_symmetry selection, a, b, c, alpha, beta, gamma, spacegroup

### PYMOL API
```python
cmd.set_symmetry(string selection, float a, float b, float c,
     float alpha,float beta, float gamma, string spacegroup)
```

###  Example
```python
1. PyMOL command line
set_symmetry 1a2p, 60, 60, 80, 90, 90, 120, P6122

1. API
cmd.set_symmetry("1a2p", 60, 60, 80, 90, 90, 120, spacegroup="P6122")
```

### NOTES
The new symmetry will be defined for every object referenced by the selection.
