# Get Dihedral

- *get_dihedral** returns the dihedral angle between four atoms.  By default, the coordinates used are from the current state, however an alternate state identifier can be provided.

By convention, positive dihedral angles are right-handed (looking down the atom2-atom3 axis).

### USAGE
```python
get_dihedral atom1, atom2, atom3, atom4 [,state ]
```

### EXAMPLES
```python
get_dihedral 4/n,4/c,4/ca,4/cb
get_dihedral 4/n,4/c,4/ca,4/cb,state=4
```

### PYMOL API
```python
cmd.get_dihedral(atom1,atom2,atom3,atom4,state=0)
```


### SEE ALSO
- Set_Dihedral
- DynoPlot
- Displaying_Biochemical_Properties#Calculating_dihedral_angles
- Rotamer_Toggle
