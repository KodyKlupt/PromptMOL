# Get names of type

- *get_names_of_type** returns a list of object and/or selection names.

### PYMOL API
```python
cmd.get_names_of_type(string type)
```

### NOTES
The object types are strings such as

- object:molecule
- object:map
- object:mesh
- object:slice
- object:surface
- object:measurement
- object:cgo
- object:group
- object:volume

###  EXAMPLES
Truncate names of all molecules

```python
1. Get names for all molecules.
for x in cmd.get_names_of_type("object:molecule"): cmd.set_name(x,x[:5])
```


### SEE ALSO
get_names, get_type, count_atoms, count_states
