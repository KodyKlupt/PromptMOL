# Volume

Volume creates a new volume object from a map object.  The data (3D scalar fields) are shown as a true 3D object using coloring and transparencies defined by the user to illustrate the data values.
This technique supports single and multiple isosurfaces.

##  Usage
 volume name, map [, ramp [, selection [, buffer [, state [, carve ]]]]]

##  Arguments
- name = the name for the new volume object.
- map = the name of the map object to use for computing the volume.
- ramp = str: named color ramp {default: }
- selection = an atom selection about which to display the mesh with an additional "buffer" (if provided).
- carve = a radius about each atom in the selection for which to include density. If "carve" is not provided, then the whole brick is displayed.

##  Example
 fetch 1oky, type=2fofc, async=0
 volume 1okyVol, 1oky_2fofc

##  Screencasts
- Silent demo movie showing the basics of loading and using a volume in PyMOL.  There are more capabilities, but this is the basic functionality.

##  Changes with PyMOL Version
- 1.4.0: first version with volume support
- 1.7.2:
- * pre-integrated volume rendering (volume_mode=1) as Incentive-PyMOL-only feature.
- * scripting support with custom color ramp (volume_color, volume_ramp_new)
- * improved volume panel, panel can be opened from the object menu ("C > panel")
- * lots of bugs fixed

##  Ray Tracing
- *There is no actual ray tracing support**. The volume rendering is implemented exclusively with OpenGL shaders. The recommended way to render a high resolution image is to use the draw command. Example:

 # render high resolution image on screen
 draw 4000, 3000, antialias=2
 png highres.png

Ray trace specific features like shadows or outlines (ray_trace_mode) are not available with this approach. If such features are needed, the ray_volume setting activates a hybrid solution, which blends the OpenGL rendered volume with the ray traced non-volume objects. Image sizes other than the current window size are not possible.

 # compose on-screen volume with ray traced image
 set ray_volume
 ray
 png composed.png

Neither of these two solutions work with headless (batch) mode.

##  Known Limitations
- No real ray-tracing support yet
- Multiple volume objects don't blend properly
