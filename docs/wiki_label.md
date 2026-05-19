# Label

The Label command controls how PyMOL draws text labels for PyMOL objects.

= Details =
Labeling is important so there are many options for your fine tuning needs.  You can change the label size, label color, positioning, font, the label outline color that masks the font and much, much more.

You can have PyMOL label atoms by properties or arbitrary strings as you want; you can even use Unicode fonts for special symbols like, \alpha, \beta, \pm, \textrm{\AA}, etc.

The following gallery shows some examples of how extensible the Label command is.

Image:Label_pre.png|Simple label
Image:New_fonts.jpeg|Example showing usage of Unicode fonts for special characters, see label_font_id.
Image:Font_ex.png|Another example with Unicode fonts
Image:Label_ex.png|Example label
Image:Ls0.png|Label shadows turned off
Image:Ls2.png|Label shadows turned on

## Built-in Object Properties
Aside from arbitrary string labels, like "This is the catalytic residue" for an atom/residue you can also use the following built-in molecular properties:
- **name**, the atom name
- **resn**, the residue name
- **resi**, the residue number/identifier
- **chain**, the chain name
- **q**, charge
- **b**, the occupancy/b-factor
- **segi**, the segment identifier
- **type** *(ATOM,HETATM)*, the type of atom
- **formal_charge**, the formal charge
- **partial_charge**, the partial charge
- **numeric_type**, the numeric type
- **text_type**, the text type

You can use one of these properties as:

```python
1. simple example: label residue 22's atoms with their names
label i. 22, name

1. Label residue #44's alpha carbon with it's residue name, residue number and B-factor.
label n. CA and i. 44, "(%s, %s, %s)" % (resn, resi, b)
```

See the syntax and examples below for more info.

=Syntax=
To use the label command follow this syntax:

```python
1. labeling syntax
label [ selection[, expression]]
```

where **selection** is some object/selection you want to label and **expression** is some string (or set of strings) which PyMOL is to use to label the given selection.

We have plenty of examples.  See the examples below.

=Settings=
Here are all the label settings and their general effect.  For each label setting, see the respective web page for more details.

- *label_angle_digits**
:: sets the number of decimals in angle label.
- *label_distance_digits**
:: sets the number of decimals in distance label.
- *label_shadow_mode**
:: sets whether or not PyMOL will ray trace shadows for your label text.  Eg:
```python
set label_shadow_mode, 2
```

- *label_color**
:: sets the color of the label text.  Note that you can have labels of different colors for different objects or selections. Some examples:

```python
1. per-object:
set label_color, color-name, object-name  #eg, set label-color, magenta, /protein

1. per-atom:
set label_color, color-name, selection    #eg, set label-color, marine, /protein/A/A/23/CA

1. another example
fragment arg
label all, name
set label_color, yellow, arg
set label_color, red, elem c
```

- *label_font_id**
:: sets the font to render your label.  There are 12 different fonts from 5&mdash;16.  Numbers 15 and 16 are special for unicode.  Eg:
```python
set label_font_id, 12
```
. See the label_font_id page for explicit examples on how to use unicode characters in PyMOL labels.
- *label_size**
:: sets the size of the text.  You can use positive numbers 2, 3, 4, etc for point sizes, or negative numbers for Angstrom-based sizes. Default is 14 points. Labels in Angstrom-size scale with the distance from the front plane, labels in point-size don't.  Eg:
```python
set label_size, -2  #results in a size of 2 Angstroms
```

- *label_digits**
:: sets the number of decimals in label. It affects all digits only if label_distance_digits or label_dihedral_digits or label_angle_digits are set to -1.
- *label_outline_color**
:: each label is outlined (so you can do white-on-white labels, for example).  This options sets the color of the label outline.  Eg.
```python
set label_outline_color, orange
```

- *label_dihedral_digits**
:: sets the number of decimals in dihedral label.
- *label_position**
:: sets any offset from the original X,Y,Z coordinates for the label.  If you like to use the mouse, you can enter edit_mode and **ctrl-left_click** to drag labels around; **ctrl-shift-left_click** will let you move the labels in the z-direction. **"Save labels"-workaround** If you want to save the position of your labels, the best way might be to create a new object and move the atoms in this object. Since the labels are positioned from the atom positions this is an indirect way of moving the labels and being able to save them.

=Examples=

```python
1. 1.
1. make a very simple label on the 14th alpha carbon.
label n. CA and i. 14, "This is carbon 14."

1. 2.
1. make a fake scene label; use this to label entire scenes, not just atoms/bonds.
pseudoatom foo
label foo, "Once upon a time..."

1. 3.
1. make a huge label
set label_size, -5
pseudoatom foo
label foo, "This is large text"

1. 4. Partial Charge
label (chain A),chain
label (n;ca),"%s-%s" % (resn,resi)
label (resi 200),"%1.3f" % partial_charge

1. 5. The gallery image above Label_ex.png was created with this code
1. and finally, some labels were moved around in **edit_mode**.
label (resi 200),"%1.3f" % b
set label_font_id, 10
set label_size, 10

1. 6. This example shows how to label a selection with the
1. XYZ coordinates of the atoms
from pymol import stored
stored.pos = []
1. select the carbon atoms in my hetero atoms to label
select nn, het and e. C
1. get the XYZ coordinates and put them into stored.pos
1. insert at the front because pop() will read the array in reverse
iterate_state 1, (nn), stored.pos.insert(0,(x,y,z))
1. label all N atoms.  You need the pop() function or else
1. PyMOL will complain b/c you didn't provide enough coords.
label nn, ("%5.5s, %5.5s, %5.5s") %  stored.pos.pop()
```

= User Comments =
## Labels Using ID Numbers
The following commnent,

```python
label SELECTION, " %s" % ID
```

labels the SELECTION with atom ID numbers.

You can make more complicated selections/lables such as

```python
label SELECTION, " %s:%s %s" % (resi, resn, name)
```

which will give you something like "GLU:139 CG"

## Labels Using One Letter Abbreviations
- First, Add this to your $HOME/.pymolrc  file:

```python
1. start $HOME/.pymolrc modification
one_letter ={'VAL':'V', 'ILE':'I', 'LEU':'L', 'GLU':'E', 'GLN':'Q', \
'ASP':'D', 'ASN':'N', 'HIS':'H', 'TRP':'W', 'PHE':'F', 'TYR':'Y',    \
'ARG':'R', 'LYS':'K', 'SER':'S', 'THR':'T', 'MET':'M', 'ALA':'A',    \
'GLY':'G', 'PRO':'P', 'CYS':'C'}
1. end modification
```

- Second, instead of:

```python
label n. ca, resn
```

use:

```python
label n. ca, one_letter[resn]
```

or: ( to get something like D85)

```python
label n. ca, "%s%s" %(one_letter[resn],resi)
```

## Labels and defer_builds_mode
If You have a weak video card, You might want to set

```python
set defer_builds_mode, 5
```

It helps a lot but breaks labels rendering. You can use

```python
set defer_builds_mode, 4
```

instead.

=See Also=
:Category:Labeling

All the settings posted above.
