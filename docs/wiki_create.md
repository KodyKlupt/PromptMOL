# Create

- *create** creates a new molecule object from a selection.  It can also be used to create states in an existing object.

### USAGE
```python
create name, (selection) [, source_state [, target_state ]]
```

- name = object to create (or modify)
- selection = atoms to include in the new object
- source_state (default: 0 - copy all states)
- target_state = int: -1 appends after last state {default: 0}

### PYMOL API
```python
cmd.create(string name, string selection, int source_state, int target_state,int discrete)
```

### NOTES
If the source and target states are zero (default), all states will be copied.  Otherwise, only the indicated states will be copied.

Target state -1 will append new states.

###  User Comments/Examples
### EXAMPLES
```python
1. merging two multi-state objects with the create command
1. obj1 has 25 states and obj2 has 40 states

load multi_state_obj1, obj1
load multi_state_obj2, obj2

1. merge the two multi-state objects back to back into obj3
1. 0 indicates every states from obj1 should be included
1. 1 indicates that the first state of obj3 is the first state from obj1 etc.

create obj3, obj1, 0, 1

1. as obj1 has 25 states, the first state of obj2 must be state 26 to create a multi-state object of obj1 and obj2 back-to-back
1. 26 indicates that the 26th state of obj3 is state nr. 1 of obj2 etc.

create obj3, obj2, 0, 26

1. Obj3 now has 65 states (25 from obj1 and 40 from obj2)
1. save obj3 as a multi-state pdb file
1. use state=0 to get all states into one pdb file

save obj3.pdb, obj3, state=0
```

### SEE ALSO
Fuse, load, copy, Extract
