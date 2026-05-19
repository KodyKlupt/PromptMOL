# Cartoon transparency

##  Overview
This setting changes the transparency of the cartoon representation.

As of PyMOL version 2.3, cartoon transparency is now an atom-level setting. This allows for a cartoon selection to be transparent without creating an additional object.

##  Syntax
```python
set cartoon_transparency, 0.5,   # 50% transparent, the object name is optional
set cartoon_transparency, 0.5,   # 50% transparent, sele: the selection name
```

Valid values range from 0.0 (fully opaque) - 1.0 (fully transparent)

##  Examples
Image:Ctt.png|Cartoon Transparency
Image:1rmm-atom-cartoon-transparency.png|Cartoon Atom-level Transparency
