# Normalize ccp4 maps

The normalize_ccp4_maps settings (default: **on**) controls whether or not PyMOL normalizes the data from a ccp4 map file **upon loading**. The data is shifted and scaled so that mean=0.0 and stdev=1.0.

Normalization is done on the raw data array, not across the unit cell. This means that if the raw data doesn't exactly cover an integral number of asymmetric units, the result will be different than for example when loading the same file into Coot, which normalizes across the cell.

- *Normalization should be turned off before loading, in cases like:**

- the map file has already been normalized, for example with CCP4’s mapmask program
- you want to specify mesh contour levels in raw units (e/A^3) instead of rmsd (sigma). This is recommended if you want to make figures that match the display in Coot.

##  Usage
```python
1. load map and normalize data
set normalize_ccp4_maps, on
load somemap.ccp4

1. load map as-is (without normalization)
set normalize_ccp4_maps, off
load somemap.ccp4
```
