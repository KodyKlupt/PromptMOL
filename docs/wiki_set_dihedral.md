# Set Dihedral

- *set_dihedral** sets a given dihedral angle given the four atoms and one angle.

### USAGE
```python
set_dihedral atom1, atom2, atom3, atom4, angle [,state=1] [,quiet=1]
```

### PYMOL API
```python
set_dihedral(string atom1,string atom2,string atom3,string atom4,float angle,state=1,quiet=1):
```

### EXAMPLES
```python
set_dihedral resi 40 and name N, resi 40 and name CA, resi 40 and  name CB, resi 40 and name CG, -180
```

### SEE ALSO
- Get_Dihedral
- DynoPlot
- Displaying_Biochemical_Properties#Calculating_dihedral_angles
- Rotamer_Toggle
