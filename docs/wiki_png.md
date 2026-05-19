# Png

- *png** writes a png format image file of the current image to disk.

##  Usage
 png filename[, width[, height[, dpi[, ray[, quiet]]]]]

- **filename** = string: file path to be written
- **width** = integer or string: width in pixels (integer or string without units), inches (in), or centimeters (cm). If unit suffix is given, `dpi` argument is required as well. If only one of `width` or `height` is given, the aspect ratio of the viewport is preserved. {default: 0 (current)}
- **height** = integer or string: height (see width) {default: 0 (current)}
- **dpi** = float: dots-per-inch {default -1.0 (unspecified)}
- **ray** = 0 or 1: should ray be run first {default: 0 (no)}
- **quiet** = 0 or 1: if 1, logged output is suppressed.  {default: 0}

##  Example
 png ~/Desktop/test.png, width=10cm, dpi=300, ray=1

##  PyMOL API
```python
cmd.png(string filename, int width=0, int height=0, float dpi=-1, int ray=0, int quiet=0)
```

##  Comments
#### Transparent Backgrounds
Use the `ray_opaque_background` setting to output images with transparent backgrounds.
 set ray_opaque_background, 0
This can be useful for presentations, images that are placed on top of a background of nonuniform color (e.g. gradients), and images that overlap text or other images.

#### DPI Setting
Use the DPI option to have PyMol set the DPI of your image.  Executing the command

```python
png /tmp/ex.png, width=1200, height=1200, dpi=300, ray=1
```

will ouput a four-inch square image at 300dpi.  Leaving off the **dpi** parameter would yield a 1200x1200 image at your system's default pixel density (e.g. 72 or 96 dpi).  This saves the intermediate step of having to use GIMP/PhotoShop/etc to rescale your photos for publication.
