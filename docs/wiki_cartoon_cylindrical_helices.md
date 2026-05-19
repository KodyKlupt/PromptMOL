# Cartoon cylindrical helices

The cartoon_cylindrical_helices setting makes cartoon helices appear as simple cylinders.

- Changed in PyMOL 2.5: Cylinders are not straight anymore but follow the actual curved shape of a helix. Straight helices are still available as mode 2.*

##  Modes
- 0: Off (helices will be rendered according to the cartoon property or settings like cartoon_fancy_helices)
- 1: Curved helices (since PyMOL 2.5)
- 2: Straight helices

##  Example
 fetch 1bb1
 set cartoon_cylindrical_helices, 1
 as cartoon

{|class="wikitable"
! set cartoon_cylindrical_helices, 1
! set cartoon_cylindrical_helices, 2
|-
|
|
|}

##  Related Settings
- cartoon_smooth_cylinder_window: half-window size for window average smoothing (mode 1)
- cartoon_smooth_cylinder_cycles: number of cycles for window average smoothing (mode 1)
- cartoon_loop_quality affects "roundness" of mode 1 curved cylindrical helices (and loops of course).
