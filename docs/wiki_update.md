# Update

- *update** transfers coordinates from one selection to another.

### USAGE
 update (target-selection),(source-selection)

### PYMOL API
```python
cmd.update( target ,source [,target_state=0 [,source_state=0 [,matchmaker=1 [,quiet=1 [,_self=cmd ]]]]]] )
```

###  ARGUMENTS
- **matchmaker** = integer: how to match atom pairs {default: 1}
- * 0: assume that atoms are stored in the identical order
- * 1: match based on all atom identifiers (segi,chain,resn,resi,name,alt)
- * 2: match based on ID
- * 3: match based on rank
- * 4: match based on index

- Note that the meaning of matchmaker=0 differs in update and fit (also rms, rms_cur, ...)!*

### EXAMPLES
 update target,(variant)

### NOTES
Currently, this applies across all pairs of states.  Fine  control will be added later.

### SEE ALSO
Cmd load
