# Volume color

volume_color set or get the volume colors.

##  Usage
 volume_color name [, ramp ]

##  Arguments
- name = str: volume object name
- ramp = str, list or empty: named ramp, space delimited string or list with (x, color, alpha, ...) or (x, r, g, b, alpha, ...) values. If empty, get the current volume colors.

##  Examples
Setting volume colors with one line:

 fetch 1a00, map, type=2fofc, async=0
 volume vol, map
 volume_color vol, .8 cyan 0. 1. blue .3 2. yellow .3

Using a named color ramp:

 volume_ramp_new cyanblueyellow, \
     .8 cyan 0. \
     1. blue .3 \
     2. yellow .3
 volume_color vol, cyanblueyellow

Getting the current volume ramp:

 PyMOL>volume_color vol
 ### cut below here and paste into script ###
 cmd.volume_ramp_new('ramp399', [\
      0.80, 0.00, 1.00, 1.00, 0.00, \
      1.00, 0.00, 0.00, 1.00, 0.30, \
      2.00, 1.00, 1.00, 0.00, 0.30, \
    ])
 ### cut above here and paste into script ###
