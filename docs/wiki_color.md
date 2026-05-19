# Color

- *color** sets the color of an object or an atom selection to a predefined, named color, an RGB hex color, or a color ramp.
For an overview of predefined colors, see Color Values.
For a script that enumerates all the colors see, List_Colors.
If you want to define your own colors, see Set_Color.

##  Usage
```python
color color-name
color color-name, object-name
color color-name, (selection)
```

##  Arguments
- color-name = str or int: named color, index of a named color, 0xRRGGBB string, 0x40RRGGBB integer, name of a ramp object, or special value atomic
- object-name = str: Name of an object or name pattern (with Asterisk (*)) which matches multiple objects. Changes the object color, and if it is a molecular object, also the color of all atoms. {default: all}
- selection = str: atom selection, this is any expression which is not a valid object pattern. E.g. an expression which starts with a parentheses. This will only color atoms, not objects.

##  Examples
### Color all carbons yellow
```python
color yellow, (name C*)
```

###  Color by element, except carbons
 color atomic, (not elem C)

###  Use a custom RGB color
 color 0x006600

### Color by Spectrum Example
Color by spectrum is in the GUI menu but did you realize that the spectrum is not limited to a simple rainbow?

```python
spectrum count, palette, object_name
```

For available palettes and more details see: spectrum

### B-Factors
The command to color a molecule by B-Factors (B Factors) is:

```python
spectrum b, selection=SEL
```

where **SEL** is a valid selection, for example, "protA and n. CA", for protein A's alpha carbons.

For more details see: spectrum

#### Reassigning B-Factors and Coloring
It is commonplace to replace the B-Factor column of a protein with some other  biochemical property at that residue, observed from some calculation or experiment.  PyMOL can easily reassign the B-Factors and color them, too.  The following example will load a protein, set ALL it's B Factors to "0", read in a list of properties for each alpha carbon in the proteins, assign those new values as the B-Factor values and color by the new values.  This example is possible because commands PyMOL  does not recognize are passed to the Python interpreter --- a very powerful tool.

```python
1. load the protein
cmd.load("protA.pdb")

1. open the file of new values (just 1 column of numbers, one for each alpha carbon)
inFile = open("newBFactors", 'r')

1. create the global, stored array
stored.newB = []

1. read the new B factors from file
for line in inFile.readlines(): stored.newB.append( float(line) )

1. close the input file
inFile.close()

1. clear out the old B Factors
alter protA, b=0.0

1. update the B Factors with new properties
alter protA and n. CA, b=stored.newB.pop(0)

1. color the protein based on the new B Factors of the alpha carbons
cmd.spectrum("b", "protA and n. CA")
```

If you want to save the file with the new B Factor values for each alpha carbon,

```python
cmd.save("protA_newBFactors.pdb", "protA")
```

or similar is all you need.

A script (data2bfactor.py) that loads data into the B-factor (b) or occupancy (q) columns from an external file can be found in Robert Campbell's PyMOL script repository (http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/)

#### Reassigning B-Factors and Coloring - from file
```python
reinitialize
prot="1XYZ"
cmd.fetch(prot,async=0)

1. Set b value to zero
cmd.alter(prot,b=0.0)
cmd.show_as("cartoon",prot)

python
inFile = open("phi_values.txt", 'r')
val_list = []
for line in inFile.readlines()[1:]:
    split = line.split()
    resn = split[0][0]
    resi = split[0][1:-1]
    phi_ppm2 = float(split[1])
    phi_ppm2_err = float(split[3])
    R2_0 = float(split[4])
    R2_0_err = float(split[6])
    print "Resn=%s Resi=%s, phi_ppm2=%2.2f, phi_ppm2_err=%2.2f, R2_0=%2.2f, R2_0_err=%2.2f"%(resn,resi,phi_ppm2,phi_ppm2_err,R2_0,R2_0_err)

    val_list.append(phi_ppm2)
    cmd.alter("%s and resi %s and n. CA"%(prot,resi), "b=%s"%phi_ppm2)

python end
minval = min(val_list)
print minval
maxval = max(val_list)
print maxval
cmd.spectrum("b", "blue_white_red", "%s and n. CA"%prot, minimum=0, maximum=maxval)
cmd.ramp_new("ramp_obj", prot, range=[0, minval, maxval], color="[blue, white, red ]")
cmd.save("%s_newBFactors.pdb"%prot, "%s"%prot)
```

###  Expanding to Surface
See Expand_To_Surface.

If you have run the above code and would like the colors to be shown in the Surface representation, too, then you need to do the following:

```python
1. Assumes alpha carbons colored from above.
create ca_obj, your-object-name and name ca
ramp_new ramp_obj, ca_obj, [0, 10], [-1, -1, 0]
set surface_color, ramp_obj, your-object-name
```

Thanks to Warren, for this one.

###  Getting Atom Colors
```python
stored.list = []
iterate all, stored.list.append(color) # use cmd.get_color_tuple(color) to convert color index to RGB values
print stored.list
```

Or, you can label each atom by it's color code:

```python
label all, color
```

###  What colors does PyMOL currently have?
basic colors can be manually accessed and edited from the PyMOL menu under **Setting** --> **Colors...**
At the Pymol prompt, you can use the command Get Color Indices to get a list of Pymols named colors.
Get_colors is a script that allows accessing colors as well.

###  Color States Individually
```python
fetch 1nmr
set all_states

1. the object has 20 states, so we can set separate line colors
1. for each state as follows:
for a in range(1,21): cmd.set("line_color","auto","1nmr",a)
```

Or, we can do it differently,

```python
1. start over,
fetch 1nmr

1. break apart the object by state
split_states 1nmr

1. delete the original
dele 1nmr

1. and color by object (carbons only)
util.color_objs("elem c")

1. (all atoms)
util.color_objs("all")
```
