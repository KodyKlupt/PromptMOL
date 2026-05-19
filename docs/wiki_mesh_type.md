# Mesh type

##  Overview
set mesh_type adjusts the way a surface mesh is displayed
 -1 nothing
 0  square grid (default)
 1  dots
At present (Pymol version 0.99rc6) type 1 does not ray trace correctly

##  Syntax
```python
set mesh_type,                           #default 0
```

##  Example
Image:min_mesh_spacing_default.jpg|mesh_type 0 square grid (default)
Image:mesh_type_1.png|mesh_type 1 dots
Image:mesh_type_1_ray.jpg|mesh_type 1 dots (raytrace attempt)
