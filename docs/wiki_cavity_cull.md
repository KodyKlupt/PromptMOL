# Cavity cull

##  Overview
set cavity_cull allows the user to define how sensitive pymol it to detecting cavities within the interior of a molecule.  Smaller cavities are not detected as the cavity cull value is increased. The value *may* correspond in angstroms a dimension of the cavity approximately.

##  Syntax
```python
1. default 2
set cavity_cull,
```

##  Example
Image:cavity_0.jpg|cavity_cull 0
Image:cavity_default.jpg|cavity_cull 2 (default)
Image:cavity_20.jpg|cavity_cull 20
