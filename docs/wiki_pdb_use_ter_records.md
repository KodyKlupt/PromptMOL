# Pdb use ter records

When a molecule (e.g. a protein molecule) is saved in pdb format by PyMOL, a line of TER record is inserted wherever the residue id is not sequential. To suppress this feature, set pdb_use_ter_records value to 0 before saving protein molecules.

##  Example
```python
get pdb_use_ter_records  # return current value of pdb_use_ter_records
set pdb_use_ter_records, 0
```

##  PyMOL API
```python
cmd.set('pdb_use_ter_records', 0)
```
