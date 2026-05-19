# Pdb conect nodup

##  Overview
The **pdb_conect_nodup** setting in pymol controls if duplicated connectivity record (CONECT) in saved PDB is used to stored bond order.

This is an unofficial PDB feature to store bond order and is supported by several applications that read PDB files, but may break PDB file loading in other applications which don't support it. PyMOL always wrote duplicated connect records (pdb_conect_nodup=0) and the setting allows you to switch that off (pdb_conect_nodup=1).

##  Syntax
```python
get pdb_conect_nodup     # get current value
set pdb_conect_nodup, 1  # no CONECT duplication is used to store bond order
```
