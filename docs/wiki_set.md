# Set

set is one of the most utilized commands.  PyMOL representations, states, options, etc. are changed with **set**.  Briefly, set changes one of the PyMOL state variables.  Currently there are over *600* PyMOL settings!

=USAGE=

```python
1. set **name** to **value**
set name, [,value [,object-or-selection [,state ]]]

1. alternative way to do the above.
set name = value  # (DEPRECATED)
```

=PYMOL API=

```python
cmd.set ( string name,
    string value=1,
    string selection='',
    int state=0,
    int updates=1,
    quiet=1)
```

= EXAMPLES =

```python
set surface_color, red

set ray_trace_mode, 3

set ribbon_width, 4

1. set the label size to 2Ang.
set label_size, -2
```

=NOTES=
The default behavior (with a blank selection) changes the global settings database.  If the selection is 'all', then the settings database in all individual objects will be changed.  Likewise, for a given object, if state is zero, then the object database will be modified.  Otherwise, the settings database for the indicated state within the object will be modified.

If a selection is provided, then all objects in the selection will be affected.
=SEE ALSO=
Get
