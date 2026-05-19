# Set name

- *set_name** can be used to change the name of an object or selection.

Not only can you simply rename an object or selection, but this command is also a powerful tool for those who deal with multiple structures in one file --- say a collection of NMR models.  The user can execute the Split_States command and then rename the molecule of choice in the state of choice.  For example, if one loads an NMR structure (with, say, 20 states) and aligns it to another structure, the balance of the alignment will (most likely) be off due to the weighting of the 19 other structures you probably don't see.  To overcome this problem, one simply executes Split_States and then renames one of the states and then aligns that newly renamed object.

### USAGE
 set_name old_name, new_name

### PYMOL API
```python
cmd.set_name(string old_name, string new_name)
```

## User Comments/Examples
```python
cmd.set_name("example", "nicename")
```

As the order of arguments is different from, for example, the Select command (where the desired name for the selection is the first argument), it may be helpful to think of this as similar to the 'mv' shell command, where the existing object is listed first and the destination second.

To batch-rename several objects with an appended number at once, use:

```python
for a in range(1,999):cmd.set_name("example"+str(a), "nicename"+str(a))
```

### SEE ALSO
get_names, get_legal_name, get_unused_name
