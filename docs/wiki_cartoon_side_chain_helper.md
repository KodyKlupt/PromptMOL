# Cartoon side chain helper

##  Overview
set **cartoon_side_chain_helper** is an easy way, in cartoon mode, to only show the side chain of a residue.

For residues represented in cartoon (but not ribbon) form, if you show the residue also in stick or wireframe **cartoon_side_chain_helper** hides backbone atoms. Showing the sidechain in this method distorts the cartoon shape so it joins with the sidechain, effectively over-riding any cartoon_flat_cycles setting for that residue.

##  Syntax
```python
set cartoon_side_chain_helper, off
set cartoon_side_chain_helper, 0              #off

set cartoon_side_chain_helper, on
set cartoon_side_chain_helper, 1              #on

1. in PyMOL 2.1, object or selection must be provide
set cartoon_side_chain_helper, on, polymer
set cartoon_side_chain_helper, 1, polymer              #on
```

##  Example
Image:cartoon_side_chain_helper_on.png|cartoon_side_chain_helper on
Image:cartoon_side_chain_helper_off.png|cartoon_side_chain_helper off

= See Also=
Ribbon_side_chain_helper
