# Intra fit

- *intra_fit** fits all states of an object to an atom selection in the specified state.  It returns the rms values to python as an array.

### USAGE
```python
intra_fit (selection),state
```

### PYMOL API
```python
cmd.intra_fit( string selection, int state )
```

### EXAMPLES
####  Simple Selection
```python
intra_fit ( name ca )
```

####  Fitting NMR Ensembles
Warren provided a great example on the PyMOL list.  If the NMR ensemble has all the structures loaded as multiple states (which is the default behavoir (see split_states) for multimodel PDBs) then we can simply call:

```python
print cmd.intra_fit(selection, state)
```

which will fit all of the other states to the indicated states and return the RMS values as a list.

A simple example is:

```python
fetch 1i8e, async=0
print cmd.intra_fit("1i8e////CA", 1)

1. results:
[-1.0, 1.1934459209442139, 1.2950557470321655, 0.71329855918884277,
0.76704370975494385, 0.78973227739334106, 0.99323123693466187,
1.0165935754776001, 0.6535714864730835, 0.95591926574707031,
1.1299723386764526, 0.28637325763702393, 0.69836461544036865,
0.40816938877105713, 1.1637680530548096]
```

Note that a RMS value of -1.0 is returned for the target state.

### PYTHON EXAMPLE
```python
from pymol import cmd
rms = cmd.intra_fit("(name ca)",1)
```

### USER EXAMPLES
### USER COMMENTS
See Rms for selection caveats for this group of commands.

### SEE ALSO
Fit, Rms, Rms_Cur, Intra_Rms, Intra_Rms_Cur, Pair_Fit, Extra_fit, Align
