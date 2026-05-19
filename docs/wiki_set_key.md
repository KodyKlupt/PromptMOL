# Set Key

- *set_key** binds a Python function or PyMOL command to a key press.
Such key binding customization is typically done with your pymolrc startup script.

- Changes with PyMOL version:*

- 1.8: decorator support
- 1.7: second argument can also be a string in PyMOL command syntax

##  PyMOL API
```python
cmd.set_key(string key, function fn, tuple arg=(), dict kw={})
```

- Also supported since PyMOL 1.7:*

```python
cmd.set_key(string key, string command)
```

- Decorator support since PyMOL 1.8:*

```python
cmd.set_key(string key)(function fn)
```

##  PyMOL Command (since PyMOL 1.7)
 set_key key, command

##  Examples
```python
from pymol import cmd

1. define a custom function which colors a selection blue
def make_it_blue(selection): cmd.color("blue", selection)

1. color "object1" blue when the F1 key is pressed
cmd.set_key( 'F1' , make_it_blue, [ "object1" ] )
```

```python
1. zoom on everything
cmd.set_key( 'CTRL-C' , cmd.zoom )
```

```python
1. turn camera by 90 degrees
cmd.set_key( 'ALT-A' , cmd.turn, ('x',90) )
```

 # zoom on first ligand when pressing F1 (PyMOL 1.7+)
 set_key F1, zoom byres (first organic), animate=1

```python
1. zoom on first ligand when pressing F1 (all PyMOL versions)
cmd.set_key('F1', cmd.zoom, ['byres (first organic)'], {'animate': 1})
```

```python
1. decorator syntax (PyMOL 1.8+)
@cmd.set_key('F1')
def zoom_ligand():
    cmd.zoom('byres (first organic)', animate=1)
```

##  KEYS WHICH CAN BE REDEFINED
 F1 to F12
 left, right, pgup, pgdn, home, insert
 CTRL-A to CTRL-Z
 ALT-0 to ALT-9, ALT-A to ALT-Z
