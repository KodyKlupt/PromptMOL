# Get object matrix

=Overview=
Pymol stores a transformation matrix for each object relative to it's initial position when loaded in.  **get_object_matrix** will return a list of floats with that matrix for a named object.

The matrix is 4X4, with the upper left 3x3 forming a rotation matrix, the fourth column and row representing pre-rotation and post-rotation translation vectors respectively, and the 16th element always being 1.0.

According the pymol source code, this is an "unsupported command".

=Syntax=

```python
cmd.get_object_matrix(object, state=1)
```

=Example=

```python
cmd.load("prot1.pdb", "prot1")
cmd.load("prot2.pdb", "prot2")
cmd.super("prot1", "prot2") #align prot1 to prot 2
transformation = cmd.get_object_matrix("prot1") #translation and rotation to align the two proteins
```
