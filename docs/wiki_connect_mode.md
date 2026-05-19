# Connect mode

= Overview =
Sets how bonds are made when loading a file.

Values:
- 0 = distance-based (excluding HETATM to HETATM) and CONECT records (default)
- 1 = CONECT records
- 2 = distance-based, ignores CONECT records
- 3 = distance-based (including HETATM to HETATM) and CONECT records
- 4 = for loading mmCIF: use the chemical components dictionary to look up bonds (*in PyMOL 1.7.4, **components.cif** needs to be present in the current directory, later versions have a subset of the dictionary bundled with PyMOL, and look up unknown residues from a web service*)

= Syntax =

```python
1. ignore CONECT records
set connect_mode, 2
1. show current setting
get connect_mode
```

= See Also =
Load, Connect_cutoff, Connect_bonded
