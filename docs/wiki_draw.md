# Draw

- *Draw** creates an oversized and antialiased
OpenGL image using the current window.  It's like Ray but not ray traced.  Also, as now with Ray the oversized images are scaled and shown in the viewer window. As Draw doesn't ray trace the shadows of the scene, it is **far** faster than ray.

##  Usage
 draw [ width [, height [, antialias ]]]

##  Examples
 draw 1600
will create an 1600-pixel wide image with an aspect ratio equal to that of
the current screen.

 draw 2000, 1500, 0
will create a 2000 by 1500 pixel image with antialiasing disabled

 draw 600, 400, 2
will create a 600 by 500 pixel image with maximum (16X) antialiasing

##  Match ray tracing appearance
Since PyMOL 1.6, all "line"-type representations can be rendered as cylinders if shaders are available and all ***_as_cylinders** settings are set. Example:

 set line_as_cylinders
 set nonbonded_as_cylinders
 set ribbon_as_cylinders
 set mesh_as_cylinders
 set dash_as_cylinders
 set render_as_cylinders
 draw 3000, 2000
