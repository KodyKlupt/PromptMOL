# Sphere scale

## Overview
This setting affects the apparent radius of spheres in the sphere representation. Default scale is set to 1.0.

## Syntax
```python
1. set the sphere scale to size for selection.
cmd.set ("sphere_scale", size=1, selection='', state=0, updates=1, log=0, quiet=1)
1. generally it's simpler to use the console form
set sphere_scale, size, selection
1. you can print the current value for sphere_scale
get sphere_scale
```

- size* can be any floating point number, *selection* is the name of a selection.

## Examples
Using 0.25 gives a nice balls&sticks representation with both lines and spheres turned on.

```python
set_bond stick_color, white, (all), (all)
set_bond stick_radius, 0.14, (all), (all)
set sphere_scale, 0.25, (all)
show sticks
show spheres
```

- *set sphere_scale** by itself will revert to default. Here you'll get a simple VDW rapresentation.

```python
set_bond stick_color, blue, (all), (all)
set_bond stick_radius, 0.3, (all), (all)
set sphere_transparency, 0.3
set sphere_scale
```

## Related settings
- sphere_color
- sphere_mode
- sphere_point_max_size
- sphere_point_size
- sphere_quality
- sphere_solvent
- sphere_transparency
