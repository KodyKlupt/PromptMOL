# Texture fonts

= Overivew =
Not sure exactly what this does.  The reason this page exists is to let the users know that this setting can affect rendering performance in PyMOL.

To test how this affects your PyMOL.  Turn on the frames per second (FPS) meter.  Load a complex scene turn on the sequence viewer (Seq_View) and then rotate the molecule.  While doing this look at the maximum frame rate.  Then turn on Texture_fonts and rotate the scene while watching the frame rate.  Here are my example numbers:
::**texture_fonts off ** max = 142 FPS
::**texture_fonts on ** max = 363 FPS

That's a huge difference.

= Syntax =

```python
1. turn on texture fonts
set texture_fonts, 1
```
