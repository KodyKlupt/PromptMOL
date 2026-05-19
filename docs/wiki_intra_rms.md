# Intra rms

- *intra_rms** calculates rms fit values for all states of an object over an atom selection relative to the indicated state.  Coordinates are left unchanged.  The rms values are returned as a python array.

### PYMOL API
```python
cmd.intra_rms( string selection, int state)
```

### PYTHON EXAMPLE
```python
from pymol import cmd
rms = cmd.intra_rms("(name ca)",1)
```

### USER COMMENTS
See Rms for selection caveats for this group of commands.

### SEE ALSO
Fit, Rms, Rms_Cur, Intra_Fit, Intra_Rms_Cur, Pair_Fit
