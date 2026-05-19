# Remove Picked

- *remove_picked** removes the atom or bond currently picked for editing.

### USAGE
 remove_picked [hydrogens]

### PYMOL API
```python
cmd.remove_picked(integer hydrogens=1)
```

### NOTES
- This function is usually connected to the DELETE key and "CTRL-D".
- By default, attached hydrogens will also be deleted unless hydrogen-flag is zero.

### SEE ALSO
Attach, Replace
