# Set bond

Set_bond sets properties on *bonds*.  This is usually some atom-connecting property like Line_width, line_color, Stick_radius.

= Syntax =

```python
1. set settingName to value for object or selection objSel
set_bond settingName, value, objSel
```

= Examples =

```python
1. Example
load $TUT/1hpv.pdb
remove het
as lines
color blue
set_bond line_with, 5, i. 1-10
```

= See Also =
- Set
- Line_width
- Stick_radius
