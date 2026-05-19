# Delete

- *delete** removes objects or selections matching an expression *name*, which can include wildcards.

### USAGE
```python
delete name
delete all   # deletes all objects
```

name = name of object or selection

### PYMOL API
```python
cmd.delete(string name = object-or-selection-name )
```

Note that special care needs to be taken to ensure that the object or selection name does not contain any quotes when passed as an argument.

### SEE ALSO
Remove
