# System

The **system** command, executes a command in a subshell under Unix or Windows.

### USAGE
```python
1. execute 'command'
system command
```

### PYMOL API
```python
cmd.system(string command,int async=0)
```

### NOTES
async can only be specified from the Python level (not the command language)
- if async is 0 (default), then the result code from "system" is returned in r
- if async is 1, then the command is run in a separate thread whose object is returned

### SEE ALSO
ls, cd, pwd
