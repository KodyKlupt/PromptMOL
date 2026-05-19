# Stereo Mode

The stereo_mode setting sets the type of stereo mode, if the stereo setting is enabled.

- You can also control both settings with the stereo command, which is more convenient!*

##  Syntax
```python
set stereo_mode, integer
```

Valid values for the **integer** argument are listed in the following table.

##  Supported Stereo Modes
Corresponding keyword arguments (instead of numeric values) can be passed to the stereo command.

{| border=1 cellspacing=0 cellpadding=4 class=wikitable
! value !! description
|-
| 1 || **quad-buffered**
|-
| 2 || **cross-eyed**
|-
| 3 || **walleye**
|-
| 4 || **geowall**
|-
| 5 || **sidebyside**
|-
| 6 || **stencil by row**, Zalman
|-
| 7 || **stencil by col**
|-
| 8 || **stencil checkerboard**
|-
| 9 || **stencil custom** for developers
|-
| 10 || **anaglyph** (requires green/magenta glasses)
|-
| 11 || **dynamic polarization**
|-
| 12 || **clone dynamic**
|}
