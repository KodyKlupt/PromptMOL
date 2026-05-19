# Fetch

- *Fetch** retrieves a protein structure from the PDB and loads it into PyMOL.
The PDB file is saved in fetch_path, which defaults to the current working directory for PyMOL.

To download a so-called biological assembly or biological unit, use the assembly setting or use *type=pdb1*, *type=pdb2* and so on.

##  Usage
 fetch codes [, name [, state [, finish [, discrete [, multiplex [, zoom [, type [, async ]]]]]]]]

##  Arguments
- **codes** = str: one or more accession codes, separated by spaces
- **name** = str: new object name {default: accession code}
- **type** = cif|mmtf|pdb|pdb1|2fofc|fofc|emd|cid|sid|cc: file type and/or accession code type {default: negotiated by code or use fetch_type_default}
- **async** = 0/1: Download structures in the background and do not block the PyMOL command line. **For scripting, you typically need async=0.** {default: 0 since PyMOL 2.3, before that: !quiet, which means 1 for the PyMOL command language, and 0 for the Python API}

- Other arguments: See load command.*

##  Proxy Setting
If your network requires a proxy server, you can specify it by 'http_proxy' and 'ftp_proxy' environmental variables. At least in Mac OS X, these values are setup automatically. Otherwise, add to your pymolrc script:

```python
import os
os.environ["http_proxy"] = "http://username:password@proxy.server.name:port/"
os.environ["ftp_proxy"] = os.environ["http_proxy"]
```

##  Examples
###  Example
```python
1. fetch them singly
fetch 1kao
fetch 1ctq

1. fetch them at once
fetch 1kao 1ctq

1. fetch them at once, load them into PyMOL all at once (synchronously)
fetch 1kao 1ctq, async=0

1. multiple commands in one line is accepted
fetch 1kao, async=0; as cartoon

1. Example loading a protein and its electron density map
fetch 1cll
fetch 1cll, type=2fofc
1. focus on residues 30-40
map_trim *, i. 30-40, 4
zoom i. 30-40
```

###  Example 2
```python
1. fetch PDB files and process each of them
1. using async=0, PyMOL will wait for fetch to finish before executing the next command
fetch 1kao, async=0
remove not (alt ''+A)
alter all, alt=''
save 1koa_clean.pdb,1koa
delete 1koa
fetch 1ctq, async=0
remove not (alt ''+A)
alter all, alt=''
save 1ctq_clean.pdb,1ctq
```

###  Example 3 - pdb1
```python
1. fetch the biological assembly of 1avd
1. the assembly is composed of asymmetric units (ASUs) stored in different MODELs
1. split the biological assembly using split_state
fetch 1avd, type=pdb1
split_state 1avd
```

###  Example 4 - multistate
This will fetch the biological assembly (type=pdb1) from the pdb, split the 60 states into separate objects (multiplex=1), and tell PyMOL to wait for all this to be completed before moving to the next command in a .pml script (async=0).

```python
1. fetch the biological assembly of 2buk
fetch 2buk, type=pdb1, multiplex=1, async=0
```
