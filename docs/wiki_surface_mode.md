# Surface mode

Sets how PyMOL draws the surface.  The default, surface_mode=0 does not include the heteroatoms within the surface; setting it to 1, does include them.  See the example images.

##  Usage
 set surface_mode, int

where *int* is one of the following values:

- 0: Default mode, surfacing with respect to flags.
- 1: Surface everything, including HET and hydrogens
- 2: Surface only heavy atoms
- 3: Surface only visible
- 4: Surface visible and heavy

##  Examples
Image:sm0.png|surface_mode set to 0, the default.  The galactose (blue) is not considered part of the surface.
Image:sm1.png|surface_mode set to 1 -- now including heteroatoms.  The galactose and all heteroatoms (blue) are now considered part of the surface and colored blue.

```python
1. make the above images, or something like them
fetch 2v72, async=0
color wheat
color marine, het
show surface

1. default
set surface_mode, 0

1. non default
set surface_mode, 1
```
