# Connect cutoff

connect_cutoff is a global setting for distance-based bonding when loading a file. Default value is 0.35.

Two atoms with VDW radii vdw1 and vdw2 are connected with a bond, if the following inequality is true:

 distance <= connect_cutoff + (vdw1 + vdw2)/2

Special cutoff adjustments are made for hydrogens (connect_cutoff - 0.2) and disulfides (connect_cutoff + 0.2).
