# Disable

The **disable** command toggles off the display of all currently visible representations of an object.  It is the equivalent of deselecting the object in the list in the top panel of the Internal GUI.

### USAGE
 disable [name]

; name
:    the name of an object or a named selection (default="all")

### PYMOL API
```python
cmd.disable( string name='all' )
```

### EXAMPLES
 disable my_object
 disable (my_object1 or my_object2)
 disable my_object*
 disable

### SEE ALSO
Show, Hide, Enable, Suspend_updates
