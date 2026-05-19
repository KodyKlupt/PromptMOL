# Load CGO

- *cmd.load_cgo()** loads Compiled Graphics Objects into the PyMOL session.  CGOs are defined by lists of floating point numbers that define either a series of triangles/vertices and colors, or one of several predefined sequences that describe mathematical shapes.

### PYMOL API
```python
cmd.load_cgo(object, name)
```

### ARGUMENTS
- **object : list of floats** Coordinate data for the CGO.
- **name : string** Name of the object (for the internal GUI)

### SEE ALSO
CGO Shapes
