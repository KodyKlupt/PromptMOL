# Matrix reset

The matrix_reset command resets the transformation for an object.

##  Usage
 matrix_reset name [, state [, mode ]]

##  Arguments
- **name** = str: object name
- **state** = int: object state {default: 1}
- **mode** = int: {defualt: -1 = matrix_mode or 0}
- * 0: transformation was applied to coordinates
- * 1: reset TTT matrix (movie transformation)
- * 2: reset state matrix

##  Example
 fetch 1akeA 4akeA, async=0

 # transform 4akeA by superposing it to 1akeA
 align 4akeA, 1akeA

 # undo the transformation
 matrix_reset 4akeA
