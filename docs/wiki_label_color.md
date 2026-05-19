# Label color

##  Overview
Sets the color that PyMol uses to draws/renders labels.  This can be set for all objects/selections or for one in particular.

##  Syntax
```python
1. set object's color to colorName
set label_color, colorName, object

1. example showing two different objects
1. each with their own coloring.
pseudoatom foo
label foo, "foo"
pseudoatom another
label another, "Another label"
set label_color, green, foo
set label_color, lightpink, another
translate [0, -10, 0], object=another
set label_size, -2
zoom foo or another, 10
```

= User Comments =
If the coloring of the labels is not *exactly* the same as you'd expect (say black turns out grey, or red turns out pink), then try the following settings:

```python
unset depth_cue
unset ray_label_specular
```

= See Also =
Color_Values, :Category:Coloring
