# Viewport

- *viewport** changes the size of the viewing port--the visible openGL window (and thus the size of all png files subsequently output).

No API command can reliably retrieve the viewport dimensions under all circumstances. However, it is possible to obtain the dimensions using a third party image viewer like Gimp or OS X Preview:

1. Save the current view as a png file ("png imagename.png").
1. Determine the image dimensions using a viewer program.

These dimensions can be applied directly using the viewport command or the API.

### USAGE
 viewport width, height

### PYMOL API
```python
cmd.viewport(int width, int height)
```
