# Hide

- *hide** conceals atom and bond representations for a certain selection or other graphical objects like distances.

Image:Show1.png|Some normal scene, notice the waters shown as spheres
Image:Show2.png|*hide spheres* issues and the spheres are now hidden.

The available representations are:
- lines
- spheres
- mesh
- ribbon
- cartoon
- sticks
- dots
- surface
- labels
- nonbonded
- nb_spheres

### USAGE
```python
hide representation [,object]
hide representation [,(selection)]
hide (selection)
```

### PYMOL API
```python
cmd.hide( string representation="", string selection="")
```

### EXAMPLES
```python
1. hides all lines
hide lines,all

1. hides all ribbons
hide ribbon

1. hides all distances
hide dashes

1. hides sticks in protA and all residues that aren't in the range of 40-65
hide sticks, protA and not i. 40-65

1. hide hydrogen atoms
hide (hydro)  # or hide (h.)
```

### SEE ALSO
Show, Enable, Disable, Suspend_updates
