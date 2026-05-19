# Delete states

- *delete_states** removes states from a multi-state object like a trajectory.

### USAGE
```python
delete_states name, 1 2 3  # delete states 1, 2, and 3
delete_states name, 1-3 9-13  # delete states 1 through 3 and 9 through 13
```

name = name of object or name expression (wildcard supported)

### PYMOL API
```python
delete_states(name: str, states: str) -> None
```

```python
cmd.delete_states(string name = object-name, string states = states string)
```

### EXAMPLES
    delete_state 1nmr, 1-5     # delete states 1 to 5 from 1nmr
    delete_state *, 1-3 10-40  # deletes states 1 to 3 and 10 to 40 from all applicable objects

Note that special care needs to be taken to ensure that the object or selection name does not contain any quotes when passed as an argument.

Note This function currently only applies to non-discrete multistate molecular objects.

### SEE ALSO
Remove
Delete
