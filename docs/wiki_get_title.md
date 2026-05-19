# Get Title

- *get_title** retrieves a text string to the state of a particular object which will be displayed when the state is active.  This is useful for printing the names of objects (given a state).

## USAGE
```python
get_title object,state
```

## PYMOL API
```python
cmd.get_title(string object, int state)
```

##  Example
Print out all the object names of the ensemble of states loaded in:

```python
for x in range(numStates):
  print cmd.get_title("objName", x)
```
