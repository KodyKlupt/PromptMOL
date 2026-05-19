# Identify

- *identify** returns a list of atom IDs corresponding to the ID code of atoms in the selection.

##  PYMOL API
```python
list = cmd.identify(string selection="(all)",int mode=0)
```

### NOTES
- mode 0: only return a list of identifiers (default)
- mode 1: return a list of tuples of the object name and the identifier
