# Iterate

The **iterate** command executes a Python expression for all atoms in a selection. The local namespace exposes all atomic identifiers and properties as read-only Python variables. The global namespace by default is the **pymol** module namespace, and thus exposes objects like **cmd** and **stored**. The order of iteration is that of the internal atom ordering.

The **alter** command is equivalent to **iterate**, but provides read-write access to the exposed variables. This can for example be used to rename a chain or to assign new b-factors. If changing identifiers which would affect atom ordering, calling sort is necessary to reorder based on the new identifiers.

The **iterate_state** command is similar to **iterate**, but iterates over the coordinates in the given state and selection, and exposes **x, y, z** in addition to the atomic identifiers and properties.

The **alter_state** command is equivalent to **iterate_state**, but allows modification of **x, y, z** (and atom-state level settings in Incentive PyMOL 1.7+).

##  Exposed Variables
All commands in the **iterate**-family expose the following variables:

- **model** (str): the object name (appearing in the selection panel on the right) (cannot be altered)
- **name** (str): the atom name
- **resn** (str): the residue name
- **oneletter** (str): **resn** translated to one letter code, like it's displayed in the sequence viewer (cannot be altered, alter **resn** instead) (PyMOL 1.8.7+)
- **resi** (str): the residue identifier (residue number) as a string, including optional insertion code
- **resv** (int): the residue identifier (residue number) as an integer, excluding insertion code
- **chain** (str): the chain name
- **alt** (str): alternate location identifier
- **elem** (str): the chemical element
- **q** (float): occupancy
- **b** (float): the B Factor
- **segi** (str): segment identifier (columns 73-76 in PDB file)
- **type** (str: ATOM,HETATM): the atom type (PDB convention for canonical polymer residues)
- **formal_charge** (int): the formal charge of the atom
- **partial_charge** (float): the partial charge of the atom
- **numeric_type**
- **text_type** (str): automatic mol2 atom typing (Incentive PyMOL 1.4+)
- **stereo** (str): automatic stereochemical R/S label (Incentive PyMOL 1.4+)
- **ID** (int): PDB atom id (not guaranteed to be unique)
- **rank** (int): atom index from original file import (not guaranteed to be unique)
- **index** (int): internal atom index (unique per object, sensitive to sorting and removing of atoms, cannot be altered)
- **vdw** (float): Van der Waals radius
- **ss** (str): secondary structure
- **color** (int): color index
- **reps** (int): numeric mask of shown representations (PyMOL 1.7.4+)
- **protons** (int): (PyMOL 1.7.4+)
- **p** (object): property object to access user-defined properties like **p.abc** (Incentive PyMOL 1.7+)
- **s** (object): settings object to access settings, e.g. **s.sphere_scale** (Incentive PyMOL 1.7+, Open-Source PyMOL 1.8.1+)
- **label** (str): see label
- **geom** (int): 1=single, 2=linear, 3=planar, 4=tetrahedral (see set_geometry)
- **valence** (int): expected number of bonds (?)
- **flags** (int): bitmask, see flag
- **cartoon** (int): see cartoon

The **iterate_state** and **alter_state** commands in addition expose:

- **x** (float): x-coordinate
- **y** (float): y-coordinate
- **z** (float): z-coordinate
- **state** (int): (PyMOL 1.7.0+)

##  Usage
 iterate (selection), expression

 iterate_state state, (selection), expression

 alter (selection), expression

 alter_state state, (selection), expression

###  Arguments
- **state** = int: object state, -1 for current state, 0 for all states
- **selection** = str: atom selection
- **expression** = str: expression in Python language

##  Examples
###  Example: Print b-factors
The following prints the atom names (**name** variable) and b-factors (**b** variable) for residue #1.

```python
iterate (resi 1), print(name + " %.2f" % b)
```

###  Example: Get b-factor list
The following example fills a list, **stored.bfactors** with the f-factors (**b** variable) from residue #1.

```python
stored.bfactors = []
iterate (resi 1), stored.bfactors.append(b)
print(stored.bfactors)
```

###  Example: Get coordinates
```python
stored.coords = []
iterate_state 1, (all), stored.coords.append([x,y,z])
```

###  Example: Modify coordinates
This example shifts the selection by 10 Angstrom along the model x-axis.

```python
alter_state 1, (all), x += 10.0
rebuild
```

###  Example: Rename chain
This renames chain **A** to **C**. Note the difference between the selection syntax (first argument) and the Python syntax with the quoted string (second argument). The sort call is necessary if let's say there is also a chain B, and you expect chain B to appear before chain C (formerly A) in the sequence viewer.

```python
alter chain A, chain="C"
sort
```

###  Example: Sequence numbering offset
Assume the residue numbering in a PDB file starts at 100, then the following updates the residue numbers to start at 1.

```python
alter (chain A), resv -= 99
sort
```

###  Example: Net Charge
The following example calculates the net charge of an object.

```python
stored.net_charge = 0
iterate (all), stored.net_charge += partial_charge
print('Net charge: ' + str(stored.net_charge))
```

###  Example: Color transfer
Copy (transfer) the color from one object to another

```python
stored.colors = {}
iterate obj1, stored.colors[chain,resi,name] = color
alter obj2, color = stored.colors.get((chain,resi,name), color)
recolor
```

##   PYMOL API
```python
cmd.iterate(str selection, str expression, int quiet=1, dict space=None)

cmd.iterate_state(int state, str selection, str expression, int quiet=1, dict space=None)

cmd.alter(str selection, str expression, int quiet=1, dict space=None)

cmd.alter_state(int state, str selection, str expression, int quiet=1, dict space=None)
```

###  Arguments
- **state** = int: state-index if positive number or any of these:
- * **state** = 0: all states
- * **state** = -1: current state
- **selection** = str: atom selection
- **expression** = str: expression in valid python syntax
- **space** = dict: namespace dictionary {default: pymol namespace}
- **atomic** = 0/1: provide atomic properties as variables if 1, or only x/y/z if 0 (in older PyMOL versions, atomic=0 gives some speed improvement) {default: 1}

###  "space" argument
The **space** argument can be used to pass local objects into the expression namespace, instead of evaluating the expression in the global **pymol** module namespace.

The b-factor list example from above but without the global pymol.stored variable:

```python
myspace = {'bfactors': []}
cmd.iterate('(all)', 'bfactors.append(b)', space=myspace)
```

User defined functions can also be included in the namespace:

```python
def myfunc(resi,resn,name):
    print('%s`%s/%s' % (resn ,resi, name))

myspace = {'myfunc': myfunc}
cmd.iterate('(all)', 'myfunc(resi,resn,name)', space=myspace)
```
