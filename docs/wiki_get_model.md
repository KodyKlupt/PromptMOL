# Get Model

- *get_model** returns a model object.

### PYMOL API
```python
cmd.get_model(string "selection", integer "state" )
```

### USAGE
 cmd.get_model("chain A")

### NOTES
It can be useful to loop through all the atoms of a selection (rather than using the iterate command)

```python
atoms = cmd.get_model("chain A")
for at in atoms.atom:
    print("ATOM DEFINITION: "+at.model+" "\
                             +at.chain+" "\
                             +at.resn+" "\
                             +str(at.resi)+" "\
                             +at.name+" "\
                             +str(at.index)+" "\
                             +"%.2f " % (at.b)\
                             +str(at.coord[0])+" "\
                             +str(at.coord[1])+" "\
                             +str(at.coord[2]))
```

### SEE ALSO
