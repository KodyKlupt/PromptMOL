# Fetch type default

When downloading structures from the wwPDB with the fetch command, the fetch_type_default setting defines what file format will be downloaded. The setting can be overruled with the **type** argument.

- New in PyMOL 1.8.6*

##  Values
- **cif** (default)
- **mmtf**
- **pdb**
- **pdb1**

##  Examples
 set fetch_type_default, mmtf
 fetch 1rx1
