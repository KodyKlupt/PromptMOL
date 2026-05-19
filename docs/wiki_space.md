# Space

Space selects a color palette (or color space).  Current choices are 'RGB', 'CMYK' (usually used in printing) and, 'pymol'.

Whereas computer displays use the RGB color space, computer printers typically use the CMYK color space.  The two spaces are non-equivalent, meaning that certain RGB colors cannot be expressed in the CMYK space and vice-versa.  And as a result, molecular graphics images prepared using RGB often turn out poorly when converted to CMYK, with purplish blues or yellowish greens.   "space cmyk" forces PyMOL to restrict its use of the RGB color space to subset that can be reliably converted to CMYK using common tools such as Adobe Photoshop.  Thus, what you see on the screen is much closer to what you will get in print.

Analog video systems as well as digital video compression codecs based on the YUV color space also have incompatibilities with RGB.  Oversaturated colors usually cause the most problems.

Although PyMOL lacks "space yuv", "space pymol" will help PyMOL avoid oversaturated colors can cause problems when exporting animations to video.

= USAGE =

```python
space space
```

- *space**
::the color space from which to choose.  Options are, 'rgb', 'cmyk' or 'pymol'.  The default is 'RGB'.

= EXAMPLES =

```python
space rgb
space cmyk
space pymol
```



=PYMOL API=

```python
cmd.space(string space)
```


=SEE ALSO=
Color, Coloring Pages, Publication Quality Pages
