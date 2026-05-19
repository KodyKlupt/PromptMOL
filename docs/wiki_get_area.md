# Get area

- *get_area** calculates the surface area in square Angstroms of the selection given. Note that the accessibility is assessed in the context of the object(s) that the selection is part of. So, to get the surface areas of e.g. a component of a complex, you should make a new object containing a copy of just that component and calculate its area.

The "get_area selection" command will return the effective surface area of the dots that you would see from "show dots, selection".  This is a discrete approximation -- not an exact calculation.

- *Attention:** Atoms with the "ignore" flag may lead to unexpected results. Clear the "ignore" flag first or exclude those atoms from the calculation.
- Fixed in PyMOL 2.5, ignored atoms are now excluded. Previously, their entire sphere surface was added to the surface area.*

= Usage =

 get_area [ selection [, state [, load_b ]]]

##  Arguments
- **selection** = str: atom selection {default: all}
- **state** = int: object state {default: 1}
- **load_b** = 0/1: Load the surface area per atom into the b-factor {default: 0}

##  Settings
The following PyMOL settings control how **get_area** works:

{| class="wikitable"
|-
! Setting
! Description
|-
| dot_solvent
| **0** = calculate **molecular surface** area {default}
- *1** = calculate **solvent accessible surface** area (SASA)
|-
| dot_density
| 1-4 {default: 2}. Sampling density. Higher density (more dots) means higher accuracy but slower performance.
|-
| solvent_radius
| The solvent radius {default: 1.4}
|}

The dot_hydrogens setting is **not** used.

For example:

```python
PyMOL> load $TUT/1hpv.pdb
PyMOL> show dots, resn arg
PyMOL> get_area resn arg
cmd.get_area: 1147.956 Angstroms^2.
PyMOL>set dot_solvent, on
PyMOL>get_area resn arg
 cmd.get_area: 673.084 Angstroms^2.
PyMOL>set dot_density, 3
PyMOL>get_area resn arg
 cmd.get_area: 674.157 Angstroms^2.
PyMOL>set dot_density, 4
PyMOL>get_area resn arg
 cmd.get_area: 672.056 Angstroms^2.
PyMOL>get_area all
 cmd.get_area: 13837.804 Angstroms^2.
```


This code has not been recently validated though it was checked a couple years back. We suggest that people perform some kind of independent check on their system before trusting the results.

##  Python API
```python
float cmd.get_area(str selection="(all)", int state=1, int load_b=0)
```

= Examples =
##  Example 1 - starting with a complex in a single file
```python
1. load complex
1. Haemoglobin in this example illustrates careful use of selection algebra
load 2HHB.pdb

1. create objects for alpha1, beta1 and alpha1,beta1 pair of subunits
create alpha1, 2HHB and chain A
create beta1, 2HHB and chain B
create ab1, 2HHB and chain A+B

1. get hydrogens onto everything (NOTE: must have valid valences on e.g. small organic molecules)
h_add

1. make sure all atoms including HETATM within an object occlude one another, but ignore solvent
flag ignore, none
flag ignore, solvent

1. use solvent-accessible surface with high sampling density
set dot_solvent, 1
set dot_density, 3

1. measure the components individually storing the results for later
alpha1_area=cmd.get_area("alpha1")
beta1_area=cmd.get_area("beta1")

1. measure the alpha1,beta1 pair
ab1_area=cmd.get_area("ab1")

1. now print results and do some maths to get the buried surface
print alpha1_area
print beta1_area
print ab1_area
print (alpha1_area + beta1_area) - ab1_area
```

##  Example 2 - starting with two components in separate files
```python
1. load components separately
load my_ligand.pdb
load my_target.pdb

1. get hydrogens onto everything (NOTE: must have valid valences on the ligand...)
h_add

1. make sure all atoms including HETATM within an object occlude one another but ignore solvent
flag ignore, none
flag ignore, solvent

1. use solvent-accessible surface with high sampling density
set dot_solvent, 1
set dot_density, 3

1. measure the components individually
ligand_area=cmd.get_area("my_ligand")
target_area=cmd.get_area("my_target")

1. create the complex
create my_complex, my_ligand my_target

1. measure the complex
complex_area=cmd.get_area("my_complex")

1. now print results
print ligand_area
print target_area
print complex_area
print (ligand_area + target_area) - complex_area
```

## Example 3 - using load_b to get surface area per atom
```python
1. example usage of load_b
1. select some organic small molecule
select ligand, br. first organic
1. get its area and load it into it's b-factor column
get_area ligand, load_b=1
1. print out the b-factor/areas per atom
iterate ligand, print b
```

## Example 4 - using a Python script to compute the SASA for individual residues
```python
import __main__
__main__.pymol_argv = ['pymol','-qc']
import pymol
from pymol import cmd, stored
pymol.finish_launching()

cmd.set('dot_solvent', 1)
cmd.set('dot_density', 3)

cmd.load('file.pdb')  # use the name of your pdb file
stored.residues = []
cmd.iterate('name ca', 'stored.residues.append(resi)')

sasa_per_residue = []
for i in stored.residues:
    sasa_per_residue.append(cmd.get_area('resi %s' % i))

print sum(sasa_per_residue)
print cmd.get_area('all')  # just to check that the sum of sasa per residue equals the total area
```

= See Also =
- For an example of **load_b** in use check out FindSurfaceResidues.
- Surface, most notably Surface#Calculating_a_partial_surface.
