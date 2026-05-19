# Group

The Group command creates or updates a "group" object.  The grouped objects are collected underneath a **+** sign in the object tree (see images) in the Pymol Internal Gui.

Group is tremendously helpful with multi-state or multi-structure sessions.  Wildcards work great, for example:

```python
1. put all of objState into the group "ensemble".
group ensemble, objState*
```

Image:group_off.png|Three EF-Hand proteins loaded into PyMOL
Image:group_on1.png|Applied the group command to the proteins via: "group efHand, *"
Image:group_on2.png|The plus was clicked and expanded to show the hierarchy of objects.

##  Usage
```python
group name, members, action
```

Actions:

- **add** - Add member to group
- **remove** - Remove members from group
- **open** - Open the group in the panel so objects can be dragged in
- **close** - Close the group in the panel so nothing can be dragged in
- **toggle** - Switch between open or close based on current state
- **auto** - (Deprecated)
- **ungroup** - (Deprecated) use the ungroup command instead
- **empty** - Move members to top level but do not delete groups
- **purge** - Delete members but do not delete groups
- **excise** - Delete groups but do not delete members
- **raise** - (Incentive 3.1+ only) Move the specified group to the top level, relevant for groups within groups

##  Examples
###  Creating, opening and closing
```python
group efHand, 1cll 1ggz 1sra

1. allow addition and removal from the group
1. If a group is open, objects can be added to or removed from
1. it by right-click+drag from the control panel
group efHand, open
1. disallow addition/removal from the group
group efHand, close
```

###  More advanced usage of groups and naming
```python
1. names with dots are treated special

set group_auto_mode, 2

1. load the example protein

load $TUT/1hpv.pdb, 1hpv.other

1. create the new entry called ".protein" in group 1hpv

extract 1hpv.protein, 1hpv.other and polymer

1. create ".ligand in the 1hpv group

extract 1hpv.ligand, 1hpv.other and organic

1. supports wildcards

show sticks, *.ligand

hide lines, *.protein

show surface, *.protein within 6 of *.ligand

show lines, byres *.protein within 4 of *.ligand

set two_sided_lighting

set transparency, 0.5

set surface_color, white

1. Also, to lexicographically sort the names in the control panel:

order *, yes
```
