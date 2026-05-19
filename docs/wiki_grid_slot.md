# Grid slot

##  Overview
Sets the grid slot location for a given object.

##  Syntax
```python
set grid_slot, int, obj
```

where **int** is the number of the grid slot and **obj** is the object to put there.

Additionally, multiple objects can be assigned to the same grid slot by simply specifying different objects to the same grid slot.  For example, if you have four objects loaded into PyMOL (A, B, C, D) and you want to show objects A and B in one slot while C and D are in another. Object E is shown in all slots by setting slot to -2:

```python
set grid_slot, 1, A
set grid_slot, 1, B
set grid_slot, 2, C
set grid_slot, 2, D
set grid_slot, -2, E
```

One use for this representation is in the context of structure prediction/validation (CASP) where you may want to show how your structure looks with respect to the native strucutre versus how somebody else's structure looks with respect to the native.  Using grid_slot (as shown) will allow for a clearer, side-by-side comparison rather than the traditional superimposition of all three structures.
