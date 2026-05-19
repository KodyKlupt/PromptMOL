# Get Pdbstr

- *get_pdbstr** is an API-only function which returns a pdb corresponding to the atoms in the selection provided and that are present in the indicated state

### PYMOL API ONLY
```python
cmd.get_pdbstr( string selection="all", int state=0 )
```

#### NOTES
1. **state** is a 1-based state index for the object.
1. if state is zero, then current state is used.

### EXAMPLES
The following example lists the residues in the selection called, **near**.

```python
import cmd # -- if required
select near, sel01 around 6
cmd.get_pdbstr("near")
```
