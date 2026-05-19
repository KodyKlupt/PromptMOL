# Ray trace disco factor

The ray_trace_disco_factor setting has an effect on ray_trace_mode 1-3. With small values, outlines will appear at surface curvature discontinuities.

{|class="wikitable"
|-
! set ray_trace_disco_factor, 0.0
! set ray_trace_disco_factor, 1.0
|-
|
|
|-
|
|
|-
|
|
|}

##  Usage
 set ray_trace_mode
 set ray_trace_disco_factor, 1.0 ;# disable effect
 set ray_trace_disco_factor, 0.1 ;# some outlines
 set ray_trace_disco_factor, 0.0 ;# strong outlines

##  Example
 # load a molecule
 fragment indane
 show_as spheres

 # white background makes black outlines
 bg_color white

 # enable outline mode
 set ray_trace_mode, 3
 set ray_trace_disco_factor, 0.0
 ray
