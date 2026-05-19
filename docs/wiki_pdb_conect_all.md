# Pdb conect all

When saving a PDB file, the pdb_conect_all settings controls whether PyMOL writes CONECT records for all bonds, or only for HETATM bonds.

PDB files by convention do not contain bond information for standard polymer residues (ATOM records), because the connectivity is known for those.

If a PDB file contains at least one CONECT record for two atoms from ATOM records, then PyMOL will set **pdb_conect_all=on** as an object-level setting, to again write CONECT records for all bonds when saving that object to a PDB file.

##  Values
- **off** turns the feature off, CONECT records are written for HETATM bonds only
- **on** turns the feature on, CONECT records are written for all bonds

##  Example
The PDB file for 1rx1 contains 52 CONECT records (for the ligands).

```python
fetch 1rx1, async=0
set pdb_conect_all, on
save 1rx1_conect_all.pdb
```

Now the file **1rx1_conect_all.pdb** contains 1316 CONECT records.
