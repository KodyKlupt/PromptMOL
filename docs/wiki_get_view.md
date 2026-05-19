# Get View

- *get_view** returns and optionally prints out the current view information in a format which can be embedded into a command script and can be used in subsequent calls to **set_view**.

If a log file is currently open, get_view will not write the view matrix to the screen unless the "output" parameter is 2.

This command is very useful for saving the orientation of a scene for later.  Authors of molecular movies may find this command very powerful.

### USAGE
 get_view

### PYMOL API
```python
cmd.get_view(output=1, quiet=1)

my_view = cmd.get_view()
```

output control:
- 0 = output matrix to screen
- 1 = don't output matrix to screen
- 2 = force output to screen even if log file is open
- 3 = return formatted string instead of a list

### API USAGE
```python
cmd.get_view(0) # zero option suppresses output (LEGACY approach)
cmd.get_view(quiet=1) # suppresses output using PyMOL's normal "quiet" parameter.
```

### NOTES
Contents of the view matrix
- 0  -  8 = column-major 3x3 matrix which rotates model axes to camera axes
- 9  - 11 = origin of rotation relative to the camera in camera space
- 12 - 14 = origin of rotation in model space
- 15      = front plane distance from the camera
- 16      = rear plane distance from the camera
- 17      = orthoscopic flag (not implemented in older versions)

### SEE ALSO
Set View, View, Model_Space_and_Camera_Space
