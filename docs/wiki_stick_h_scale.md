# Stick h scale

The stick_h_scale setting scales the stick radius of bonds to hydrogens.

- Default value changed in 1.8.4*

##  Example
 fragment trp
 as sticks
 set stick_h_scale, 0.4

 # before 1.8.4 this was only in effect with a negative stick_radius
 set stick_radius, -0.25
