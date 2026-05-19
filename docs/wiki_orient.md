# Orient

- *orient** aligns the principal components of the atoms in the selection with the XYZ axes.  The function is similar to the orient command in X-PLOR.

### USAGE
 orient object-or-selection [, state]
 orient (selection)

### PYMOL API
```python
cmd.orient( string object-or-selection [, state = 0] )
```

### NOTES
   state = 0 (default) use all coordinate states
   state = -1 use only coordinates for the current state
   state > 0  use coordinates for a specific state

### EXAMPLES
For models with NCS symmetry, orient will align the model with the symmetry axis centered along the viewport's z axis.  For example,

   fetch 1hiw, async=0
   as cartoon
   remove (!chain A,B,C)
   orient
   util.cbc

will produce the first image below.  However, if there is a larger symmetry, e.g. two trimers, this will not work.  In the above example, leaving out remove (!chain A,B,C) from the script results in the second image below.

Image:1hiw orient.png|One trimer from 1hiw after "orient" command.
Image:1hiw orient2.png|Both trimers from 1hiw after "orient" command.

### SEE ALSO
Zoom, Origin, Reset
