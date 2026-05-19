# Cartoon smooth loops

## Overview
This is a display setting. When set to off, the cartoon will follow a path that is splined between each alpha carbons. This sometimes yields representations that are pretty frizzy. Turning this setting on will make the cartoon follow a smoother (but less conservative) path so that the representation is easier on the eyes. Use with caution, since false conclusions can be drawn by solely examining a smoothed cartoon trace. It is always best (for non-representation purposes) to also have a line trace so that the backbone is precisely located.

Image:Frizz.JPG|set cartoon_smooth_loops,0 : the cartoon passes through each alpha-carbon
Image:Smooth.JPG|set cartoon_smooth_loops,1 : the cartoon is straighter but less conservative

- *NOTE:** If changing the setting that is set by a *preset* command (like "Publication"), ie.
```python
set cartoon_smooth_loops,0
```
 does not seem to have any effect, then you may need to unset the property on your object, ie
```python
unset cartoon_smooth_loops,obj
```
.

### Sticks and Smooth Loops
When **cartoon_smooth_loops** is turned **on** and sticks are shown for some residue selection, often times the sticks don't touch the backbone or cartooned elements.  To fix this, turn this setting **off** or enable **cartoon_side_chain_helper**.  See the images below for an example.

Image:Csl_on.png|Cartoon Smooth Loops ON
Image:Csl_off.png|Cartoon Smooth Loops OFF

Also, of note for this problem is Cartoon_flat_sheets.

## Syntax
turn on:
 set cartoon_smooth_loops, 1
turn off:
 set cartoon_smooth_loops, 0

### Additional remarks
I do not know precisely how the smoothed trace is generated, probably by some splining mode. Could someone more knowledgeable than me edit to be more precise ?
