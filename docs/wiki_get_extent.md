# Get Extent

- *get_extent** returns the minimum and maximum XYZ coordinates of a selection as an array:

```
[ [ min-X , min-Y , min-Z ],[ max-X, max-Y , max-Z ]]
```

Typing this command returns the coordinates for all atoms. To return the coordinates of the default selection type:

```
get_extent sele
```

### PYMOL API
```python
cmd.get_extent(string selection="(all)", state=0 )
```
