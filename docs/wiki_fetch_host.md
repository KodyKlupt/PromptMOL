# Fetch Host

The **fetch_host** setting controls from which PDB server you download files when using the fetch command.  You options are:
- pdb
- pdbe
- pdbj
- mirror URL with "divided" layout *(new in PyMOL 1.6)*

for the standard RCSB (pdb), pdb mirror in europe, and the pdb mirror in Japan.

- New in PyMOL 1.3*

##  Details
The exact URL (or list of URLs to try) is stored in pymol.importing.hostPaths[type]. The **fetch_host** setting only applies to the incomplete (not starting with scheme://) URL entries there.

##  Usage
 set fetch_host, pdb
 set fetch_host, pdbe
 set fetch_host, pdbj
 set fetch_host, http://ftp.wwpdb.org/pub/pdb
 set fetch_host, file:///local/mirror/pub/pdb

```python
1. Paths which are appended to fetch_host
import pymol
pymol.importing.hostPaths["cif"] = "/data/structures/divided/mmCIF/{mid}/{code}.cif.gz"
pymol.importing.hostPaths["pdb"] = "/data/structures/divided/pdb/{mid}/pdb{code}.ent.gz"
```

```python
1. Don't use fetch_host, use a custom URL
import pymol
pymol.importing.hostPaths["cif"] = "http://files.rcsb.org/download/{code}.{type}.gz"
pymol.importing.hostPaths["pdb"] = "http://files.rcsb.org/download/{code}.{type}.gz"
```
