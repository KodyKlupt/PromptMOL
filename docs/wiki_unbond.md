# Unbond

- *unbond** removes all bonds between two selections.

Image:Unbond1.png|Atoms bound normally, but not the representation we want.
Image:Unbond2.png|Atoms unboud with the unbound command.

=USAGE=

```python
unbond atom1,atom2
```

=PYMOL API=

```python
cmd.unbond(selection atom1="(pk1)",selection atom2="(pk2)")
```

= Example =

```python
1. remove all bonds in residue 999 to residue 999
1. this command was used in the examples above in PDB ID 1ACO.
unbond i. 999, i. 999
```

=SEE ALSO=
Bond, Fuse, Remove_picked, Attach, Detach, Replace
