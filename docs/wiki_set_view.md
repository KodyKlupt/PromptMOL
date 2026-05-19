# Set View

- *set_view** sets viewing information for the current scene, including the rotation matrix, position, origin of rotation, clipping planes, and the orthoscopic flag.

This command is extremely useful for making movies.  One may set up the scene to be rendered, then save the exact orientation, with respect to the camera, of the scene using, the Get_View command.  The output from the Get_View command may then be used by the **set_view** command to restore the orientation of the scene.

### USAGE
 set_view (...)  where ... is 18 floating point numbers

### EXAMPLE
This works in a .pml script:

    set_view (\
        0.999876618,   -0.000452542,   -0.015699286,\
        0.000446742,    0.999999821,   -0.000372844,\
        0.015699454,    0.000365782,    0.999876678,\
        0.000000000,    0.000000000, -150.258514404,\
        11.842411041,   20.648729324,    8.775371552,\
        118.464958191,  182.052062988,    0.000000000 )

### PYMOL API
```python
cmd.set_view(string-or-sequence view)
```


####  Example
This works in a .py script:

```python
cmd.set_view((
    0.999876618,   -0.000452542,   -0.015699286,
    0.000446742,    0.999999821,   -0.000372844,
    0.015699454,    0.000365782,    0.999876678,
    0.000000000,    0.000000000, -150.258514404,
    11.842411041,   20.648729324,    8.775371552,
    118.464958191,  182.052062988,    0.000000000))
```

The result of get_view is valid input for **set_view**:

```python
myview = cmd.get_view()

cmd.set_view(myview)
```

### NOTES
Contents of the view matrix

- 0  -  8: column-major 3x3 matrix which rotates model axes to camera axes
- 9  - 11: origin of rotation relative to the camera in camera space
- 12 - 14:  origin of rotation in model space
- 15: front plane distance from the camera
- 16: rear plane distance from the camera
- 17: orthoscopic flag (not implemented in older versions)

### SEE ALSO
Get View, View
