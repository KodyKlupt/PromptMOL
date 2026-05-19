# Pdb echo tags

pdb_echo_tags sets the field(s) to be displayed in the overlay/console window upon loading a PDB file.

= Usage =

```python
1. example usage, display HEADER,TITLE and COMPND fields
1. The syntax of the final field is a quoted, comma-separated list of PDB fields.
set pdb_echo_tags, "HEADER,TITLE,COMPND"
```

Default value is "HEADER,TITLE,COMPND".
See PDB file format documentation for possible fields.
