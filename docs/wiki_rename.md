# Rename

- *rename** creates new atom names which are unique within residues.

### USAGE
#### CURRENT
```python
rename object-name [ ,force ]
force = 0 or 1 (default: 0)
```

#### PROPOSED
```python
rename object-or-selection,force
```

### PYMOL API
#### CURRENT
```python
cmd.rename( string object-name, int force )
```

#### PROPOSED
```python
cmd.rename( string object-or-selection, int force )
```

### NOTES
To regerate only some atom names in a molecule, first clear them with an "alter (sele),name=''" commmand, then use "rename"

### SEE ALSO
alter

Or for rename an object
set_name
