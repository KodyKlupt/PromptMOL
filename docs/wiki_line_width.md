# Line width

= Overview =
Controls the width that PyMOL draws lines.

Image:lw1.png|Line width set to default
Image:lw2.png|Line width set to 10 on residues 1-10 and then colored those residues red.

= Sytnax =

```python
1. set line width
set line_width, value

1. set line_width to value for object or selection, objSel
set_bond line_width, value, objSel

1. Example
load $TUT/1hpv.pdb
as lines
set line_width, 10

1. or on a bond-by-bond basis,
set_bond line_width, 7, i. 20-30
```

= See Also =
- Set
- Set_bond
