# Map auto expand sym

## OVERVIEW
When **map_auto_expand_sym** is ON, symmetry operations will be applied to expand it
beyond the precalculated volume when necessary.

## USAGE
 set map_auto_expand_sym, on

The default is ON.

## Note
isomesh, isosurface, etc use symmetry information (lattice constants, space group) of the
model specified by *selection* argument if available, or (new in 1.7) from the map object.
