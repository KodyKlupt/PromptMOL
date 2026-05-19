# Zoom

- *zoom** scales and translates the window and the origin to cover the atom selection.

### USAGE
 zoom [ selection [,buffer [, state [, complete ]]]]

### EXAMPLES
```python
1. auto zoom depending on what's loaded in PyMOL
zoom

1. zoom complete=1

1. zoom on just chain A
zoom (chain A)

1. zoom on residue 142
zoom 142/

1. zoom consistenly 20 Ang from each object at the center
center prot1
zoom center, 20

1. prot1 and prot2 will have the same exact zoom factor
center prot2
zoom center, 20
```

### PYMOL API
```python
cmd.zoom( string selection, float buffer=0.0,
          int state=0, int complete=0 )
```

### NOTES
 state = 0 (default) use all coordinate states
 state = -1 use only coordinates for the current state
 state > 0  use coordinates for a specific state

 complete = 0 or 1:

Normally the zoom command tries to guess an optimal zoom level for visualization, balancing closeness against occasional clipping of atoms out of the field of view.  You can change this behavior by setting the complete option to 1, which will guarantee that the atom positions for the entire selection will fit in the field of an orthoscopic view.  To absolutely prevent clipping, you may also need to add a buffer (typically 2 A) to account for the perspective transformation and for graphical representations which extend beyond the atom coordinates.

### SEE ALSO
- Origin
- Orient
- Center
