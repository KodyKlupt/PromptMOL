# Wizard

- *wizard** launches one of the built-in wizards.  There are special Python scripts which work with PyMOL in order to obtain direct user interaction and easily peform complicated tasks.

### USAGE
```python
wizard name
```

### PYMOL API
```python
cmd.wizard(string name)
```

### EXAMPLE
```python
wizard distance  # launches the distance measurement wizard

1. set a message
cmd.wizard("message", "Hello, I'm a message.")

1. dimiss the message
cmd.wizard()
```
