# View

- *view** makes it possible to save and restore viewpoints on a given scene within a single session.

### USAGE
```python
view key[,action]
view *
```

key can be any string
action should be 'store' or 'recall' (default: 'recall')

### PYMOL API
```python
cmd.view(string key,string action)
```

### FUNCTION KEY PRESETS
Views F1 through F12 are automatically bound to function keys provided that "set_key" has not been used to redefine the behaviour of the respective key, and that a "scene" has not been defined for that key.

### EXAMPLES
 view 0,store
 view 0

### SEE ALSO
Scene, Set View, Get View
