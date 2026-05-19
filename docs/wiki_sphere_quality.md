# Sphere quality

## Overview
- *sphere_quality** controls the rendering quality of sphere objects. This setting only affects sphere rendering when not using shaders.

## Syntax
```python
1. the default value is 1
set sphere_quality,
```

Larger values of  result in higher quality sphere rendering. Values >1 may result in poor performance during real-time rotation or translation.

- *Note**: Selecting values larger than 2 with **stick_ball** = 1 (enabled) causes PyMol to crash in the Windows version.

## Examples
Open the images to see rendering details.

Image:Sphere_quality_0.png|sphere_quality 0
Image:Sphere_quality_1.png|sphere_quality 1 (default)
Image:Sphere_quality_2.png|sphere_quality 2

= See Also =
cgo_sphere_quality
