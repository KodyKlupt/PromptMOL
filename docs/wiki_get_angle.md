# Get Angle

- *get_angle** returns the angle between three atoms.  By default, the coordinates used are from the current state, however an alternate state identifier can be provided.

### USAGE
get_angle atom1, atom2, atom3, [,state ]

### EXAMPLES
 get_angle 4/n,4/c,4/ca
 get_angle 4/n,4/c,4/ca,state=4

### PYMOL API
```python
cmd.get_angle(atom1="pk1",atom2="pk2",atom3="pk3",state=0)
```
