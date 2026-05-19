# Map Trim

- *Map Trim** introduced in PyMol 0.99beta11, gives the user the ability to cut out a section of a map and read it back in as a completely new map.  This was not previously possible prior to 0.99beta11.  (Windows build at PyMol Beta or compile from source).

##  Usage
```python
map_trim map-name, selection-name, buffer
```

Combined with the convenient new object-name wildcards (!!!), you could
for example trim all your maps to 3 Angstroms around ligands with one
commmand as follows

```python
map_trim *, organic, 3
```

With map size now reduced, the map_double command can come in handy to
increase mesh density on your figure.

```python
map_double *
```
