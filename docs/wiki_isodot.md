# Isodot

- *isodot** creates a dot isosurface object from a map object.

### USAGE
```python
isodot name = map, level [,(selection) [,buffer [, state ] ] ]
map = the name of the map object to use.
level = the contour level.
selection = an atom selection about which to display the mesh with an additional "buffer" (if provided).
```

### NOTES
If the dot isosurface object already exists, then the new dots will be appended onto the object as a new state.

### SEE ALSO
load, isomesh, Dynamic_mesh
