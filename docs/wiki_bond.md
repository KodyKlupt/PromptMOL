# Bond

- *bond** creates a new bond between two selections, each of which should contain one atom. You can easily create a new bond by selecting two atoms, each with the CTRL-MIDDLE-MOUSE-BUTTON and typing "bond" on the command line.

In order to visualize the newly created bond, lines or sticks have to be shown for both atoms.

### USAGE
 bond [atom1, atom2 [,order]]

atom1 and atom2 must either be selections (created by the select command, for example) or chosen using the PkAt mouse action (Ctrl+Middle mouse button). order is an optional integer (default is 1).

Example usage:

 bond resi 1 and name NE2, resi 10 and name ND1

### PYMOL API
 cmd.bond(string atom1, string atom2)

where atom1 and atom2 are selections.

### NOTES
The atoms must both be within the same object.

The default behavior is to create a bond between the (lb) and (rb) selections.

### SEE ALSO
Unbond, Fuse, Attach, Replace, Remove_picked
