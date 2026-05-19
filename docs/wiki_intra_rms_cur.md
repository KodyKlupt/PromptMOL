# Intra rms cur

- *intra_rms_cur** calculates rms values for all states of an object over an atom selection relative to the indicated state without performing any fitting.  The rms values are returned as a python array.

### PYMOL API
```python
cmd.intra_rms_cur( string selection, int state)
```

### PYTHON EXAMPLE
```python
from pymol import cmd
rms = cmd.intra_rms_cur("(name ca)",1)
```

### USER EXAMPLES/COMMENTS
See Rms for selection caveats for this group of commands.

### SEE ALSO
Fit, Rms, Rms_Cur, Intra_Fit, Intra_Rms, Pair_Fit
