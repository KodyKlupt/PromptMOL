# Suspend updates

When set, Suspend_updates stops PyMOL from updating the GUI whenever changes are made.  This can be used to mask multiple operations from the user to make it appear as if only one operation occurred.  See examples.

= Example =

```python
load $TUT/1hpv.pdb
set suspend_updates
1. remove the waters
remove resn HOH
1. the waters are still visible
1. until we unset suspend_updates
1. 1. Now, to get UI responsiveness type
1. 1. unset suspend_updates
```

### PYMOL API
```python
cmd.set('suspend_updates', 'on')
cmd.set('suspend_updates', 'off')
```

### SEE ALSO
Show, Hide, Enable, Disable
