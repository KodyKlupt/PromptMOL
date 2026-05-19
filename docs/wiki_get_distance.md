# Get Distance

- *get_distance** returns the distance between two atoms.  By default, the coordinates used are from the current state, however an alternate state  identifier can be provided.

### USAGE
 get_distance atom1, atom2, [,state ]

### EXAMPLES
 get_distance 4/n,4/c
 get_distance 4/n,4/c,state=4

### PYMOL API
```python
cmd.get_distance(atom1="pk1",atom2="pk2",state=0)
```

### SEE ALSO
- Distance # create a distance object
- Distancetoatom # Automated script for distances to a point
- Measure_Distance # basic script
