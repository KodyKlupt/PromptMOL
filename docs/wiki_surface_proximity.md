# Surface proximity

When showing the molecular surface of a subset of atoms (not the entire molecule), then the surface_proximity setting controls whether triangles are shown which are between an included and an excluded atom.

##  Values
- **surface_proximity=on**: (default) Show all triangles which have at least one vertex belonging to the atom selection. In this case colors from hidden atoms can leak into the open surface edge.
- **surface_proximity=off**: Show only triangles where all three vertices belong to the atom selection.

##  Example
This example demonstrates the color "leaking" from atoms which don't belong to the surface selection.

 fetch 5hpr, async=0
 color red
 color yellow, chain B
 show surface, chain B
 set surface_proximity, off
