# Get Color Indices

- *get_color_indices** in combination with **get_color_tuple** will retrieve the RGB values for colors.

```python
print cmd.get_color_indices()
```

will retrieve the Pymol color names and corresponding internal color indices. The Pymol names can be used to designate color for objects, see Color.  To retrieve a single index for a specific color name, use **get_color_index** instead.

```python
print cmd.get_color_tuple(index-number)
```
 will retrieve individual RGB components when *index-number* is replaced with one of the color indices from above.

The color index, an integer, gets returned when color is returned while employing Iterate. You can thus use the  **get_color_tuple** command above to convert that to RGB color values if you need to use the colors outside Pymol.

Tangentially related is the fact you can name additional colors,

```python
set_color color-name, [r,b,g]
```

will create a new color that will appear in the GUI list.  From the
open-source GUI you can use the "add" button in the color list viewer.
In MacPyMOL, enter the new name into the MacPyMOL color editor window,
set the RGBs, and then click Apply.
See Set Color for more details and examples.
The colors created will be added to the end of the list of Pymol's color indices that you can view the **get_color_indices()** command.

### EXAMPLES
```python
1. rename a color
cmd.set_color('myfavoritecolor', cmd.get_color_tuple(cmd.get_color_index('red')))
```
