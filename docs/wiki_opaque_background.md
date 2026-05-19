# Opaque background

= Overview =
This setting controls how PyMOL renders the background.  If this opaque setting is **on** then the background is drawn as a solid color depending on your background color setting.  If this is turned off, the background is drawn as transparent.  Transparent backgrounds allow you to post your rendered image on a background of any color without having to first to background subtraction.  This is great for posters or publications.  It also works well when your presentation background is not simply black or white.  In the PyMOL window a transparent background is shown as a checkerboard, but in your final image it will really be transparent.

= Syntax =

```python
1. set it on or off

1. solid background
set opaque_background, on

1. transparent background
set opaque_background, off
```

= See Also =
Ray
