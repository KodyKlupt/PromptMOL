# Center

- *center** translates the window, the clipping slab, and the origin to a point centered within the atom selection.

### PYMOL API
```python
cmd.center( string selection, int state = 0, int origin = 1 )
```

### NOTES
- state = 0 (default) use all coordinate states
- state = -1 use only coordinates for the current state
- state > 0  use coordinates for a specific state

- origin = 1 (default) move the origin
- origin = 0 leave the origin unchanged

##  User Example
- Center around any given point

```python
1. define the point as x=1.0, y=2.0, z=3.0; replace [1.0, 2.0, 3.0] with your coordinate.
origin position=[1.0,2.0,3.0]
1. center on it
center origin
```

### SEE ALSO
Origin, Orient, Zoom
