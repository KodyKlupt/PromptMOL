# Matrix Copy

Matrix_copy copies the object matrix from one object to another.

This command is often used after a protein structure alignment to bring other related objects into the same frame of reference.

= Usage =

```python
matrix_copy source_name, target_name
```

##  Arguments
- source_name = string: name of object to take matrix from
- target_name = string: name(s) of object(s) to copy matrix to
- source_mode = integer: 0: raw coordinates, 1: object TTT matrix, 2: state matrix, 3: camera matrix transformation {default: -1: matrix_mode setting}
- target_mode = integer: (see source_mode)
- source_state = integer: object state {default: 1}
- target_state = integer: object state {default: 1}
- target_undo = 1/0: ??? {default: 1}

= Example =
Here's a practical example. We grab two proteins and their density maps. We then align one to the other and then use matrix_copy to move over the density map:

```python
1. fetch two proteins and their maps

fetch 1rx1 3dau, async=0
fetch 1rx1 3dau, type=2fofc, async=0

1. align them proteins

align 1rx1, 3dau

1. copy 1rx1's matrix to 1rx1_2fofc
1. it's density map

matrix_copy 1rx1, 1rx1_2fofc

1. show the result

enable *
show extent, *2fofc
```

= Example =

```python
1. load two molecules
load mol1.pdb
load mol2.pdb

1. load their maps
load map1.ccp4
load map2.ccp4

1. align the two molecules
align mol2////CA, mol1////CA

1. copy mol2's map to mol2
matrix_copy mol2, map2

1. show the isomesh
isomesh mesh1, map1
isomesh mesh2, map2
```

= See Also =
 Object Matrix Matrix_reset, align, fit, and pair_fit.
