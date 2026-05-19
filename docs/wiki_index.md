# Index

- *index** returns a list of tuples corresponding to the object name and index of the atoms in the selection.

### PYMOL API
```python
list = cmd.index(string selection="(all)")
```

### NOTE
Atom indices are fragile and will change as atoms are added or deleted.  Whenever possible, use integral atom identifiers instead of indices.
