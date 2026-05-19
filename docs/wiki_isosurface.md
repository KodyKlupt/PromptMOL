# Isosurface

- *isosurface** creates a new surface object from a map object.

##  Usage
```python
isosurface name, map, [,level [,(selection) [,buffer [,state [,carve [,source_state [,side [,mode ]]]]]]]]
```

- name = the name for the new mesh isosurface object.
- map = the name of the map object to use for computing the mesh.
- level = the contour level. (default=1.0)
- selection = an atom selection about which to display the mesh with an additional "buffer" (if provided). (default="")
- state = the state into which the object should be loaded (default=1) (set state=-2 to append new surface as a new state)
- carve = a radius about each atom in the selection for which to include density. If "carve= not provided, then the whole brick is displayed. (default=None)
- source_state = the state of the map from which the object should be loaded. (default=0)
- Front or back face. Triangle-winding/normal direction. (default=1)
- mode = surface geometry (0: dots; 1: lines; 2: triangle triangle-normals; 3: triangle gradient-normals) (default=3)

##  Algorithm
PyMOL offers three different algorithms for isosurface generation. Each of these can be activated by the isosurface_algorithm setting

- 0: Marching Cubes via VTKm (default) (requires VTKm)
- 1: Marching Cubes basic (fallback if VTKm not installed)
- 2: Marching tetrahedra (legacy)

##  Examples
 fetch 1oky, type=2fofc, async=0
 isosurface 1okySurf, 1oky_2fofc

With carving at 2 Angstrom around the molecular model:

 fetch 1oky, async=0
 fetch 1oky, type=2fofc, async=0
 isosurface 1okySurf, 1oky_2fofc, 1.0, (1oky), carve=2.0
