# Centerofmass

The centerofmass command calculates the center of mass for an atom selection. It considers atom mass and occupancy.

- New in PyMOL 1.7.2. See the center_of_mass script for older PyMOL versions.*

##  Usage
 centerofmass [ selection [, state ]]

##  Arguments
- **selection** = str: atom selection {default: all}
- **state** = int: object state, -1 for current state, 0 for all states {default: -1}

##  Example
 PyMOL> fetch 1ubq, async=0
 PyMOL> centerofmass
  Center of Mass: [  30.004,  28.522,  14.701]

##  Python API
```python
cmd.centerofmass()
```

returns a list of 3 floats.
