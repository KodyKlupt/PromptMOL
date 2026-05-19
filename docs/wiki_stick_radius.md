# Stick radius

## Overview
This setting affects the radius of sticks in the sticks representation. Default scale is set to 0.25.

In newer versions of PyMOL, one may set the Stick_radius on a per-bond basis.  So, you can set for example, the radius of only selected bonds if you want.  This is done through the Set_bond command.

Image:Stick_rad_0.05.png|stick_radius set to 0.05
Image:Stick_radius_default.png|stick_radius set to the default 0.25
Image:Stick_rad_0.85.png|stick_radius set to 0.85

## Syntax
```python
set_bond stick_radius, *size*, selection
```

where,
- *size* can be any float number. Using 0.25 (default value) is usually appropriate for most representations, although 0.15 migh be preferred for comparing closely related structures, e.g., conformers.

- Note:*
```python
set_bond stick_radius
```
 by itself will revert to 1.00.
## If the above commands do not work
You can do something like below

```python
To set on the entire object

set stick_radius=0.12

OR

create myObj,

Ex : create myObj, hetatm

set stick_radius,0.2,myObj
```

## Related settings
- Set_bond
- sphere_scale
- stick_ball_ratio
