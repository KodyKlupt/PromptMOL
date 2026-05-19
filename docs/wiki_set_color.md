# Set Color

Set_Color defines a new color with color indices (0.0-1.0). Numbers between 0 an 255 can be used as well. (If at least one value is larger than 1, pymol will interpret all 3 values as between 0 and 255). If an existing color name is used, the old color will be overridden.

### USAGE
```python
set_color name, [ red-float, green-float, blue-float ]
set_color name = [ red-float, green-float, blue-float ]  #(DEPRECATED)
```

### PYMOL API
```python
cmd.set_color( string name, float-list rgb )
```

### EXAMPLES
```python
PyMOL>set_color red, [1,0.01,0.01]
 Color: "red" defined as [ 1.000, 0.010, 0.010 ].
PyMOL>set_color khaki, [195,176,145]
 Color: "khaki" defined as [ 0.765, 0.690, 0.569 ].
```

These will be added to the end of the list of Pymol's color indices that you can view the Get Color Indices command.
