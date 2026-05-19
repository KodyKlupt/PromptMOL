# Get Names

- *get_names** returns a list of object and/or selection names.

### PYMOL API
```python
cmd.get_names(type,enabled_only,selection)
```

### ARGUMENTS
- **type : string** determines the type of objects to be returned. It can take any of the following values:
- * **objects** Structure objects
- * **selections** All selection
- * **all** Objects and Selections
- * **public_objects** (default)
- * **public_selections**
- * **public_nongroup_objects**
- * **public_group_objects**
- * **nongroup_objects**
- * **group_objects**
- **enabled_only : boolean** If 1, only enabled objects are returned. Default 0 (all objects)
- **selection**
### NOTES
The default behavior is to return only object names.

###  EXAMPLES
Multiple alignments

```python
1. structure align all proteins in PyMOL to the protein named "PROT".  Effectively a
1. poor multiple method for multiple structure alignment.
for x in cmd.get_names("all"): cealign( "PROT", x)
```


Determine whether or not an object (objName) is enabled:

```python
if objName in cmd.get_names(enabled_only=1):
    print objName, "is enabled"
```

### SEE ALSO
get_type, get_names_of_type, count_atoms, count_states
