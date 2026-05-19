# Get chains

This command will return a python list of chains for the given selection.

Proteins structures often have more than one chain of residues present in a structure file.  This command will fetch the names of each chain present.  Because of the lack of standards, sometimes chain A will also be blank "".  This isn't a problem for PyMOL, but be warned sometimes you may get back, [""].

= Syntax =

```python
1. using get_chains for the object or selection called objSel
get_chains objSel
```

= Examples =

```python
1. examples
fetch 1cll
print "1CLL has the following chains:", cmd.get_chains("1cll")

1. list all chains in all proteins loaded in PyMOL:
for x in cmd.get_names():
  for ch in cmd.get_chains(x):
    print x, " has chain ", ch
```

= See Also =
Get_Names
