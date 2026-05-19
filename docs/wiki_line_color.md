# Line color

= Overview =
Line_color controls per atom/bond coloring in objects or selections.

= Syntax =

```python
1. set the color of the lines to colorName
set line_color, colorName

1. set per atom/bond line colors (see examples)
set_bond line_color, colorName, objSel

1. example
fetch 1te1
as lines
orient
1. draw all lines red
set line_color, red
1. draw just chain A, blue
set_bond line_color, marine, blue
1. color the lysines magnesium!
set_bond line_color, magnesium, resn lys
```

= See Also =
- Set
- Set_bond
- Lines
- Line_width
