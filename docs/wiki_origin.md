# Origin

- *origin** sets the center of rotation about a selection.  If an object name is specified, it can be used to set the center of rotation for the object's TTT matrix.

### USAGE
```python
origin selection [, object [,position, [, state]]]
origin (selection)
origin position=[1.0,2.0,3.0]
```

### PYMOL API
```python
cmd.origin( string object-or-selection )
```

### NOTES
- state = 0 (default) use all coordinate states
- state = -1 use only coordinates for the current state
- state > 0  use coordinates for a specific state

### SEE ALSO
Zoom, Orient, Reset

###  Example
This example puts the camera 'inside' a protein near the ligand and turns the camera 360 degrees about that location.

```python
load $TUT/1hpv.pdb

set field_of_view, 45

zoom organic
orient organic
show stick, polymer
show surface
set surface_color, white
set transparency, 0.5
clip slab, 30
set line_width, 5

cmd.move("z",-cmd.get_view()[11])

python
def spin():
   from pymol import cmd
   for x in range(360):
      cmd.move("z",cmd.get_view()[11])
      cmd.turn("y",1)
      cmd.move("z",-cmd.get_view()[11])
      cmd.refresh()

threading.Thread(target=spin).start()
python end
```
