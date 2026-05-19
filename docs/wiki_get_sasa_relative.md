# Get sasa relative

get_sasa_relative calculates the relative per-residue solvent accessible surface area and optionally labels and colors residues.
The value is relative to full exposure of the residue, calculated by removing all other residues except its two next neighbors, if present.

The command loads a value beteween 0.0 (fully buried) and 1.0 (fully exposed) into the b-factor property, available in iterate, alter and label as **b**.

- New in Incentive PyMOL 1.8 and Open-Source PyMOL 2.1*

- Changed in PyMOL 2.6: Added **subsele** argument*

##  Usage
 get_sasa_relative [ selection [, state [, vis [, var [, quiet [, outfile [, subsele ]]]]]]]

##  Example
 fetch 1ubq
 get_sasa_relative polymer

Side-chain exposure, including C-alpha atom, using **subsele** argument (new in PyMOL 2.6):

 get_sasa_relative polymer, subsele=sidechain guide
