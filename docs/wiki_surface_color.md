# Surface color

= Overview =
- *surface_color** controls the color of surfaces as drawn in PyMOL.

Image:Surface color ex1.png|Usual surface coloring
Image:Surface color ex2.png|Color the entire surface "marine".

= Syntax =

```python
1. color the surface
set surface_color, (color), (selection)
```

= Examples =

```python
1. color the surface white
set surface_color, white, *

1. return surface coloring to the default scheme
set surface_color, default, *
```

= See Also =
Color, Color_Values
