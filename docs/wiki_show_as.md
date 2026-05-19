# Show as

show_as turns on and off atom and bond representations.

=Details=

The available representations are the usual:

(History: Python 2.6 came out with the keyword as which is also a PyMOL keyword.  So, we had to change the PyMOL-named keyword to show_as.)

- lines
- spheres
- mesh
- ribbon
- cartoon
- sticks
- dots
- surface
- labels
- extent
- nonbonded
- nb_spheres
- slice

##  USAGE
```python
show_as representation [, selection ]
```


##  ARGUMENTS
- **representation** = lines, spheres, mesh, ribbon, cartoon, sticks, dots, surface, labels, extent, nonbonded, nb_spheres, slice, extent, slice, dashes, angles, dihedrals, cgo, cell, callback, everything
- **selection** = string {default: all}

##  EXAMPLES
```python
1. show the backbone as lines
show_as lines, name ca or name c or name n

1. show everything as a ribbon
show_as ribbon
```

##  PYMOL API
```python
cmd.show_as(string representation, string selection)
```
