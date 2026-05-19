# Label shadow mode

##  Overview
Sets whether or not PyMol renders shadows casted onto labels and whether or not the labels themselves cast shadows.

Values
- 0, no shadows
- 1, object shadows are projected onto the labels, but the labels don't cast shadows
- 2, object shadows are projected onto the labels, AND the lables DO cast shadows
- 3, object shadows are NOT projected onto the labels, BUT the lables DO cast shadows.

##  Syntax
```python
set label_shadow_mode, 0  # turn off shadows projected onto lables, turn off shadows cast from labels
set label_shadow_mode, 1  # turn on shadows projected onto labels, turn off shadows cast from labels
set label_shadow_mode, 2  # turn off shadows projected onto lables, turn on shadows cast from labels
set label_shadow_mode, 3  # turn on shadows projected onto lables, turn on shadows cast from labels
```
