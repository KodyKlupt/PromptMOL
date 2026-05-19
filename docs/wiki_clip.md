# Clip

- *clip** alters the near and far clipping planes

### USAGE
 clip {near|far|move|slab|atoms}, distance [,selection [,state ]]

### EXAMPLES
 clip near, -5           # moves near plane away from you by 5 A
 clip far, 10            # moves far plane towards you by 10 A
 clip move, -5           # moves the slab away from you by 5 A
 clip slab, 20           # sets slab thickness to 20 A
 clip slab, 10, resi 11  # clip 10 A slab about residue 11
 clip atoms, 5, pept     # clip atoms in "pept" with a 5 A buffer
                         # about their current camera positions
## PYMOL API
```python
cmd.clip( string mode, float distance, string selection = None)
```
