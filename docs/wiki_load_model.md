# Load Model

- *load_model** reads a ChemPy model into an object.  If a trajectory (many models with the same name and different values for state) is being loaded, It can be used with the option discrete=1 to allow changes in the b-factors and Van der Waals radius between snapshots.

### PYMOL API
```python
cmd.load_model(model, object [,state [,finish [,discrete ]]])
```

###  See Also
Get_Model
