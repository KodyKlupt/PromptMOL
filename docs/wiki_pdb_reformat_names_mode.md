# Pdb reformat names mode

pdb_reformat_names_mode sets atom naming for PDB files as it reads them.

= Usage =

```python
1. example usage, set to amber compliant

set pdb_reformat_names_mode, 2
```

Modes:

- *0**
:: default, off
- *1**
:: PDB compliant, (eg. HH12 becomes 2HH1, etc.)
- *2**
:: amber compliant, amber compliant (eg., 2HH1 becomes HH12)
- *3**
:: pdb compliant, but use IUPAC within PyMOL
