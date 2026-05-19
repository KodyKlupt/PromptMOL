# Stereo

The stereo command sets the current stereo mode.
Stereo mode is a convenient way to "see" 3D with two images from slightly different angles.

- There are corresponding **stereo** and stereo_mode settings which are controlled by the **stereo** command, so you don't need to set them directly.*

##  Usage
```python
stereo [ toggle ]
```

Valid values for the **toggle** argument are:
on,
swap,
off,
quadbuffer,
crosseye,
walleye,
geowall,
sidebyside,
byrow,
bycolumn,
checkerboard,
custom,
anaglyph,
dynamic,
clonedynamic
(see also stereo_mode)

##  Example
```python
fetch 1ESR, async=0
as cartoon
set cartoon_smooth_loops
spectrum
bg white
stereo crosseye
```
