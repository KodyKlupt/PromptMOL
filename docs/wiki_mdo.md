# Mdo

- *mdo** sets up a command to be executed upon entry into the specified frame of the movie.  These commands are usually created by a PyMOL utility program (such as util.mrock).  Command can actually contain several commands separated by semicolons ';'

### USAGE
 mdo frame : command

### PYMOL API
```python
cmd.mdo( int frame, string command )
```

### EXAMPLE
 // Creates a single frame movie involving a rotation about X and Y
 load test.pdb
 mset 1
 mdo 1: turn x,5; turn y,5;
 mplay

```python
//Show waters within 4 Angstroms around the first residue from a 15 frame simulation trajectory
load structure.pdb
load_traj structure.dcd, structure, start=1, stop=15
mset 1 -15
for a in range(1,16): cmd.mdo(a,"hide sphere; select waters, (structure & i. 1 around 4) & resn HOH, state="+str(a)+"; show sphere, waters")
```

### NOTES
The **mset** command must first be used to define the movie before "mdo" statements will have any effect.  Redefinition of the movie clears any existing mdo statements.

### SEE ALSO
Mset, Mplay, Mstop
