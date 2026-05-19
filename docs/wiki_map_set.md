# Map set

Map_set provides a number of common operations on and between maps.  For example, with Map_set you can add two maps together or create a consensus map from a series of maps or even take a difference map.

= Usage =

```python
map_set name, operator, operands, target_state, source_state
```

operator may be,
- average
- copy
- difference
- maximum
- minimum
- sum
- unique

= Examples =

```python
1. add 3 maps
map_set my_sum, sum, map1 map2 map3

1. calculate the average map
map_set my_avg, average, map1 map2 map3
```

= Detailed Example =
This example shows you how to create a consensus map of the bound ligand in a conserved pocket.

```python
1. fetch some similar proteins from the PDB
fetch 1oky 1h1w 1okz 1uu3 1uu7 1uu8 1uu9 1uvr, async=0

1. align them all to 1oky; their ligands
1. should all now be aligned
alignto 1oky

1. highlight the ligands
as sticks, org

1. select one of the atoms in the organic small mol
sele /1uu3//A/LY4`1374/NAT

1. select entire molecules very near the chosen atom
select bm. all within 1 of (sele)

1. remove the proteins; just look at small molecules
remove not (sele)

1. create maps for all the ligands
python
for x in cmd.get_names():
  cmd.map_new( "map_" + x, "gaussian", 0.5, x)
python end

1. calculate the average map
map_set avgMap, average, map*

1. show as transparent surface
set transparency, 0.5

isosurface avgSurface, avgMap, 1.0

orient vis
```

= Notes =
source_state = 0 means all states

target_state = -1 means current state

This is an experimental function.

= See Also =
Map_new
