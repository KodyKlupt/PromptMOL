# Chromadepth

The chromadepth setting turns on color by depth, using a rainbow spectrum from red (near) to blue (far). This can produce a pseudo-stereo effect when using ChromaDepth glasses.

- New in Incentive PyMOL 1.7.6*

- New in Incentive PyMOL 1.8.6: Ray tracing support*

- In Open-Source PyMOL since 2.2.0*

##  Example
```python
fetch 1rx1, async=0
as surface
show sticks, organic

set chromadepth

set_view (\
     0.683854997,    0.728400052,   -0.042148408,\
    -0.276858896,    0.312507719,    0.908674002,\
     0.675050080,   -0.609731972,    0.415373385,\
     0.000000000,    0.000000000,  -62.658931732,\
    29.408838272,   54.024459839,   15.061312675,\
    45.707679749,   79.610176086,  -20.000000000 )

1. these settings can improve chromadepth experience
set depth_cue, 0
set specular, 0
```

##  Gallery
Image:Chroma_3d.png
Image:Chroma_3d2.png
Image:Chroma_3d3.png
Image:Chroma_3d4.png
Image:Chroma_3d5.png
