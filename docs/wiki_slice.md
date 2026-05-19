# Slice

slice creates a slice object from a map object.

##  USAGE
```python
slice_new name, map, [state, [source_state]]
```

- or*

```python
slice name, map, [state, [source_state]]
```

##  ARGUMENTS
- **name** = the name for the new slice object (string)
- **map** = the name of the map object to use for computing the slice (string)
- **state** = the state into which the object should be loaded (default=1; set state=0 to append new mesh as a new state)
- **source_state** = the state of the map from which the object should be loaded (default=0)

##  EXAMPLES
```python
1. Create a map slice plane perpendicular to current view
slice a_new_slice, a_map

1. A more complicated example that shows how to create multiple slices
1. (in this case, 3 slices perpendicular to each other), each colored
1. with a different color ramp and different contour levels:

1. Reset the view, to align view on XYZ axes
reset
1. (Optional: Adjust view direction to your liking)
1. Create a map slice *perpendicular* to the current view.
1. The slice seems to be in the center of the APBS (or other) volmap. Map "tracking" is off by default.
slice slice_A, apbs_map
1. Rotate camera 90 degrees about the vertical axis
turn y, 90
1. Second, perpendicular, slice
slice slice_B, apbs_map
1. Rotate again, this time about the horizontal
turn x, 90
1. Third slice
slice slice_C, apbs_map

1. Define new color ramps: ramp_name, map_object, list of low/mid/hi values, 3 RGB triplets
ramp_new ramp1010RWB, apbs_map, [-10,0,10], [ [1,0,0], [1,1,1], [0,0,1] ]
ramp_new ramp11RYG, apbs_map, [-1,0,1], [ [1,0,0], [1,1,0], [0,1,0] ]
ramp_new ramp55MltGO, apbs_map, [-5,0,5], [ [0,1,1], [0.5,1,0.5], [1,0.5,0.2] ]

1. Color the map slices
color ramp1010RWB, slice_A
color ramp11RYG, slice_B
color ramp55MltGO, slice_C

1. Adjust the fineness of the slice color gradations:
cmd.set('slice_grid',0.1) # normally at 0.3; much finer than 0.05 gets a bit slow

1. Map slices can be moved, relative to other fixed objects (e.g., your protein/DNA/RNA),
1. by turning tracking on (Action menu), and the using the Shift-MouseWheel to move
1. the slice forward in and backward in Z. Adjust fineness of this Z-motion with:
1. cmd.set('mouse_wheel_scale',0.05) # normally at 0.5

1. The result is shown in the image above.
```


##  PYMOL API
```python
cmd.slice_new(string slice_name, string map_name, integer state=0, integer source_state=0)
```
