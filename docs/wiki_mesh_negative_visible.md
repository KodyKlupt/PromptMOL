# Mesh negative visible

If the **mesh_negative_visible** setting is **on**, then an isomesh at iso level 3.0 will in addition show the -3.0 contour. The color of the negative contour is defined by the **mesh_negative_color** setting. The color of the positive contour is defined with the color command, or with the mesh_color setting.

The **surface_negative_visible** and **surface_negative_color** settings control the same behavior for isosurface objects.

Since PyMOL 1.8.4 the negative color can be controlled from the color menu ("C > negative > ...").

##  Example
Show the +/- 3 sigma iso-level mesh ("wire-frame") of a difference density map.

 fetch 1ubq, diffmap, type=fofc, async=0
 isomesh diffmesh, diffmap, 3.0
 color green, diffmesh
 set mesh_negative_color, red
 set mesh_negative_visible

Same, but with a closed surface:

 fetch 1ubq, diffmap, type=fofc, async=0
 isosurface diffsurf, diffmap, 3.0
 color green, diffsurf
 set surface_negative_color, red
 set surface_negative_visible

##  Color Menu
Image:A-menu-isomesh-negative.png|Action (A) menu of a map object
Image:C-menu-isomesh-negative.png|Negative color (C > negative) menu of an isomesh object
