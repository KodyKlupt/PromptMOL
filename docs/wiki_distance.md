# Distance

=Distance=
{|-
||
- *distance** creates a new distance object between two selections.  It will display all distances within the cutoff.  Distance is also used to make hydrogen bonds.
Calling distance without arguments will show distances between selections (pk1) and (pk1), which can be set in editing mode or using the PkAt mouse action (usually CTRL-middle-click).
Note: For interactive use, the **measurement** wizard (from the PyMOL menu) makes measuring distances easier than using the distance command.
If you want to measure distance and avoid creating a distance object, use Get Distance or Distancetoatom.
|

|

||
|}

=Usage=

```python
distance [ name [, selection1 [, selection2 [, cutoff [, mode ]]]]]
```

- *name**
::string: name of the distance object to create
- *selection1**
::string: first atom selection
- *selection2**
::string: second atom selection
- *cutoff**
::float: longest distance to show
- *mode**
::0: all interatomic distances
::1: only bond distances
::2: only show polar contact distances
::3: like mode=0, but use distance_exclusion setting
::4: distance between centroids (*new in 1.8.2*)
::5: pi-pi and pi-cation interactions
::6: pi-pi interactions
::7: pi-cation interactions
::8: like mode=3, but cutoff is the ratio between distance and sum of VDW radii

:: modes 5 to 8 are available only in incentive PyMOL.

=PYMOL API=

```python
cmd.distance( string name, string selection1, string selection2,
              float cutoff, int mode )
   # returns the average distance between all atoms/frames
```

### EXAMPLES
- Get and show the distance from residue 10's alpha carbon to residue 40's alpha carbon in 1ESR:

```python
1. make the first residue 0.
zero_residues 1esr, 0
distance i. 10 and n . CA, i. 40 and n. CA
```

- Get and show the distance from residue 10's alpha carbon to residue 35-42's alpha carbon in 1ESR:

```python
1. make the first residue 0.
zero_residues 1esr, 0
distance i. 10 and n . CA, i. 35-42 and n. CA
```

- This neat example shows how to create distance measurements from an atom in a molecule to all other atoms in the molecule (since PyMol supports wildcards).

```python
cmd.distance("(/mol1///1/C)","(/mol1///2/C*)")
```

or written without the PyMolScript code,
 dist /mol1///1/C, /mol1///2/C*
- Create multiple distance objects

```python
for at1 in cmd.index("resi 10"): \
   for at2 in cmd.index("resi 11"): \
       cmd.distance(None, "%s`%d"%at1, "%s`%d"%at2)
```

```python
distance (selection1), (selection2)

1. example
dist i. 158 and n. CA, i. 160 and n. CA

distance mydist, 14/CA, 29/CA
distance hbonds, all, all, 3.2, mode=2
```

=See Also=
- Get Distance # Avoid creating an object
- Distancetoatom # Automated script for distances to a point
- Measure_Distance # basic script
- Lines
