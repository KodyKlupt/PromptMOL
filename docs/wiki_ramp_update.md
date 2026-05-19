# Ramp update

ramp_update updates range and/or color of a color ramp.

- New in PyMOL 1.8*

##  Usage
 ramp_update name [, range [, color ]]

##  Example
 ramp_new    e_pot_color, e_pot_map, [-10,0,10], [red,white,blue]
 ramp_update e_pot_color, range=[-15,0,15]
 ramp_update e_pot_color, color=[green,white,orange]
