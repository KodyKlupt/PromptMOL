# Cycle Valence

- *cycle_valence** cycles the valence on the currently selected bond.

### USAGE
 cycle_valence [ h_fill ]

### PYMOL API
```python
cmd.cycle_valence(int h_fill)
```

### EXAMPLES
 cycle_valence
 cycle_valence 0

### NOTES
If the h_fill flag is true, hydrogens will be added or removed to satisfy valence requirements.

This function is usually connected to the DELETE key or "CTRL-W".  (Try CTRL-W first.)

There are two distinct ways to cycle a bond valence in PyMOL. First, if you start by clicking the Builder button you don't need to worry about Editing Mode, PyMOL will take care of that for you.  After clicking Builder, click Cycle.  In green text you should see, "Pick bonds to set as Cycle bond..." now just use the LEFT mouse button to click on a bond (not an atom). If you repeatedly click the bond, PyMOL will cycle the valence. The second method requires PyMOL to be in Editing Mode. To ensure you're in Editing Mode, please either click Mouse > 3 Button Editing.  Now, using the mouse please CTRL-RIGHT-click on a bond (not an atom).  The white cuff appears with a number (the angle of the substituents).  Last, type CTRL-w to cycle the bond.

### SEE ALSO
remove_picked, attach, replace, fuse, h_fill Edit_Keys
