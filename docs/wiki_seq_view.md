# Seq view

## Overview
The **seq_view** command turns the sequence viewer on and off. The sequence viewer is a very handy tool, you can use it for example to select residues very easily.  When the sequence viewer is turned on, you can select individual residues or multiple residues by selecting residues, using the mouse, on the sequence viewer.

- Note:* The sequence viewer, seems to decrease PyMOL's performance when very many proteins are loaded into PyMOL.  Therefore, if you have many proteins loaded, turn off the sequence viewer to increase performance if you don't need the viewer.  You can remedy this, by turning on texture_fonts.  Simply do,

```python
set texture_fonts, 1
```

## Syntax
```python
1. to turn the sequence viewer on.
set seq_view, 1

1. to turn the sequence viewer off.
set seq_view, 0
```

## Related settings
- seq_view_color
- seq_view_discrete_by_state
- seq_view_fill_char
- seq_view_fill_color
- seq_view_format
- seq_view_label_color
- seq_view_label_mode
- seq_view_label_spacing
- seq_view_label_start
- seq_view_location
- seq_view_overlay
- seq_view_unaligned_color
- seq_view_unaligned_mode
