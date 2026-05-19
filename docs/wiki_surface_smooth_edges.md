# Surface smooth edges

When the surface representation is only partially visible (e.g. ligand binding site surface),
the **surface_smooth_edges** setting controls appearance of the surface edges.

- New in Incentive PyMOL 1.8.6*

##  Values
- **surface_smooth_edges=off**: (default) disables surface edge smoothing.
- **surface_smooth_edges=on**: enables surface edge smoothing. Consecutive vertices of the surface edge are averaged resulting in smoother-looking edge.

##  Examples
 set surface_smooth_edges, off

 set surface_smooth_edges, on

 set surface_smooth_edges, off

 set surface_smooth_edges, on
