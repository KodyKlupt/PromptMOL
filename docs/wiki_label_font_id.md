# Label font id

The label_font_id setting sets the typeface (font family) for atom labels.

##  Syntax
```python
1. use "Serif Bold" font family
set label_font_id, 10
```

##  Available Font Families
- Font IDs 0-4 were fixed size GLUT fonts, their support was dropped in PyMOL 1.6.*

{| class="wikitable"
!Name!!label_font_id
|-
|Sans||5
|-
|Sans Oblique||6
|-
|Sans Bold||7
|-
|Sans Bold Oblique||8
|-
|Serif||9
|-
|Serif Oblique||17
|-
|Serif Bold||10
|-
|Serif Bold Oblique||18
|-
|Mono||11
|-
|Mono Oblique||12
|-
|Mono Bold||13
|-
|Mono Bold Oblique||14
|-
|Gentium Roman||15
|-
|Gentium Italic||16
|}

##  Special Characters
Several Unicode characters are supported.
They can be entered with unicode literals as 4-digit hexadecimal escape sequences.

- *Example characters** (find the code for your character at Unicode Charts):

{| class="wikitable"
!Code!!Character!!Name
|-
|u"\u03b1"||α||Alpha
|-
|u"\u03b2"||β||Beta
|-
|u"\u00c5"||Å||Ångström
|-
|u"\u00b1"||±||plus/minus
|-
|u"\u00b2"||²||superscript 2
|}

##  Example 1
```python
1. if Python is configured with utf-8 default encoding (all incentive builds)
label  5/CA, u"\u03b1-Helix"
label 10/CA, u"\u03b2-Sheet"

1. if Python is configured differently, explicit utf-8 encoding is necessary
label  5/CA, u"\u03b1-Helix".encode("utf-8")
label 10/CA, u"\u03b2-Sheet".encode("utf-8")

1. italic
set label_font_id, 16

1. make bigger
set label_size, 50

1. cast shadows in ray tracing
set label_shadow_mode, 3
```

##  Example 2
```python
1. label residue 30 with "4.1 Ang^2 +/- 0.65 Ang^2
label i. 30, "4.1" + u"\u00c5\u00b2  \u00b1 0.65 \u00c5\u00b2 "
```
