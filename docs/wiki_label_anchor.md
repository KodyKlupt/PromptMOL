# Label anchor

Label_anchor is a new setting that controls onto which atoms residue labels will go.  Selecting L > Label > Residues creates labels for your object or selection and they default to the alpha carbon.  You can set Label_anchor to 'CB' or any other atom type to label on that atom instead of the alpha carbon.

Note: If you set this to an atom that doesn't exist in a residue, that label will be blank.  Eg, setting this to "CB" will *not label* glycine residues.

= Usage =

```python
1. default labels will be on beta carbons now
set label_anchor, "CB"
```
