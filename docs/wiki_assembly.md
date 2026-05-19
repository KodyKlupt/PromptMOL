# Assembly

When loading **mmCIF** structure files, the assembly setting controls whether PyMOL loads the asymmetric unit (assembly="") or a biological unit (e.g. assembly="1"). Assembly identifiers in mmCIF files can be arbitrary strings, but usually are numeric and most files define at least assembly "1".

- New in PyMOL 1.8*

Assemblies with more than one symmetry copy are loaded as multi-state objects with all_states=on. The assemblies should be equivalent to the **pdb1** files which are available from the [ftp://ftp.wwpdb.org/pub/pdb/data/biounit/ PDB ftp server].

##  Examples
Download the ASU and the first assembly, show them side by side.

```python
set assembly, ""
fetch 3bw1, asu, async=0

set assembly, 1
fetch 3bw1, assembly1, async=0

set grid_mode
```
