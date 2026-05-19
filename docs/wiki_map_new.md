# Map new

map_new creates a map object using one of the built-in map generation routines.

This command can be used to create low-resolution surfaces of protein structures.

##  Usage
 map_new name [, type [, grid [, selection [, buffer [, box [, state ]]]]]]

##  Arguments
- name = string: name of the map object to create or modify
- type = vdw, gaussian, gaussian_max, coulomb, coulomb_neutral, coulomb_local {default: gaussian}
- grid = float: grid spacing {default: gaussian_resolution/3.0}
- selection = string: atoms about which to generate the map {default: (all)}
- buffer = float: cutoff {default: gaussian_resolution}
- state = integer: object state {default: 0}
- * state > 0: use the indicated state
- * state = 0: use all states independently with independent extents
- * state = -1: use current global state
- * state = -2: use effective object state(s)
- * state = -3: use all states in one map
- * state = -4: use all states independent states by with a unified extent

##  Examples
See examples for huge surfaces and isomesh.

##  Related Settings
- gaussian_resolution
- gaussian_b_adjust
- gaussian_b_floor
