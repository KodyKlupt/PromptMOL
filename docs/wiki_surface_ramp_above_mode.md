# Surface ramp above mode

The **surface_ramp_above_mode** setting is for coloring molecular surfaces by electrostatic potential, using a color ramp. If **on**, the surface is colored by the potential on the solvent accessible surface, which is one solvent radius above the surface.

Coloring with *surface_solvent=0* and *surface_ramp_above_mode=0* is less meaningful, since a solvent or ligand atom never reaches the molecular surface of the protein (only the accessible surface). Furthermore, *surface_solvent=1* with *surface_ramp_above_mode=1* isn't meaningful either.

##  Illustration
##  Example
```python
load molecule.pdb
load electrostaticmap.dx

ramp_new espramp, electrostaticmap, [ -3, 0, 3]

show surface

set surface_color, espramp
set surface_ramp_above_mode
```
