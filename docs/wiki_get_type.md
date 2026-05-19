# Get Type

- *get_type** returns a string describing the named object or selection or the string "nonexistent" if the name in unknown.

### PYMOL API
```python
cmd.get_type(string object-name)
```

### NOTES
Possible return values are
1. "object:molecule"
1. "object:map"
1. "object:mesh"
1. "object:distance"
1. "selection"

### SEE ALSO
Cmd get_names
