# Dump

The dump command writes the geometry of an isosurface, isomesh, or isodot object to a simple text file. Each line contains one vertex.

For surface objects, XYZ coordinates and the normal are exported. Three lines make one triangle (like GL_TRIANGLES).

For mesh objects, XYZ coordinates are exported (no normals). The vertices form line strips (like GL_LINE_STRIP), a blank line starts a new strip.

For dot objects, XYZ coordinates are exported.

##  Usage
 dump filename, object

##  Arguments
- filename = str: file that will be written
- object = str: object name

##  Example
 fetch 1ubq, mymap, type=2fofc, async=0

 isosurface mysurface, mymap
 dump surfacegeometry.txt, mysurface

 isomesh mymesh, mymap
 dump meshgeometry.txt, mymesh

 isodot mydot, mymap
 dump dotgeometry.txt, mydot
