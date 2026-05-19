# Show

- *Show** displays atom and bond representations for certain selections.

=Details=

Image:Ray2.png|Example of a shown surface.
Image:Ray_trace_gain2.png|Ball and sticks shown.
Image:Mesh_w05.png|A cartoon inside a mesh shown.

The **Show** command, is one of the most often used commands in PyMOL.  For example, you can *show* certain atoms as *Lines* or *Sticks* or *Cartoons* or any of the following representations:
- lines
- spheres
- mesh
- ribbon
- cartoon
- sticks
- dots
- surface
- label
- extent
- nonbonded
- nb_spheres
- slice
- cell

## USAGE
 show
 show reprentation [,object]
 show reprentation [,(selection)]
 show (selection)

## PYMOL API
```python
cmd.show( string representation="", string selection="" )
```

## EXAMPLES
#### Example
```python
1. show the backbone using lines.
show lines,(name ca or name c or name n)
```

#### Example
```python
1. show the ribbon representation for all objects
show ribbon
```

#### Example
```python
1. show all hetero atoms as spheres
show spheres, het
```

#### Example
```python
1. show only polar hydrogens
hide everything, ele h
show lines, ele h and neighbor (ele n+o)
1. hide nonpolar hydrogens
hide (h. and (e. c extend 1))
```

Note:

The above code hides all representations of nonpolar hydrogens, including surface representations, resulting in broken surface representations.  It might be better to remove the nonpolar hydrogens instead:

```python
1. show only polar hydrogens
hide everything, ele h
show lines, ele h and neighbor (ele n+o)
1. remove nonpolar hydrogens
remove (h. and (e. c extend 1))
```
