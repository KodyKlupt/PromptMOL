# Unset

- *unset** behaves in two ways.

If selection is not provided:

- Since PyMOL 2.5: Changes the named global setting to the default value.
- Before PyMOL 2.5: Changes the named global setting to a zero or off value.

If a selection is provided, then "unset" undefines object-specific or state-specific settings so that the global setting will be in effect.

##  Usage
 unset name [,selection [,state ]]

##  Python API
```python
cmd.unset ( string name, string selection = '',
         int state=0, int updates=1, int log=0 )
```
