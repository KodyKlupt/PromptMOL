# Ribbon color

## Overview
Ribbon_color allows one to explicitly state the color to be applied to a ribbon object.

## Syntax
```python
1. set it to a color
set ribbon_color, color

1. examples:
1. default auto-cycles the color for each new object
set ribbon_color, marine

1. apply green to the ribbon only for object obj01
set ribbon_color, green /obj01

1. apply orange to the ribbon only for chain B of object obj01; NB: not fully enabled until version 1.0
set ribbon_color, orange /obj01//B
```

## Examples
Image:ribbon_color_green.png|ribbon_color green
Image:ribbon_color_marine.png|ribbon_color marine
Image:ribbon_color_chains.png|two chains in same object with different colors

## Advanced details
Some notes on general Set syntax (From PyMOL "help set"):

DESCRIPTION

   "set" changes one of the PyMOL state variables,

USAGE

   set name, [,value [,object-or-selection [,state ]]]

   set name = value  # (DEPRECATED)

PYMOL API

   cmd.set ( string name, string value=1,
             string selection='', int state=0,
              int updates=1, quiet=1)

NOTES

   The default behavior (with a blank selection) changes the global
   settings database.  If the selection is 'all', then the settings
   database in all individual objects will be changed.  Likewise, for
   a given object, if state is zero, then the object database will be
   modified.  Otherwise, the settings database for the indicated state
   within the object will be modified.

   If a selection is provided, then all objects in the selection will
   be affected.
