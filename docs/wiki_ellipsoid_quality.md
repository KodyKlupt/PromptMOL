# Ellipsoid quality

= Overview =
This setting determines how much refinement PyMOL uses in rendering ellipsoids.  Other representations have similar settings.  The most often used is Surface_quality.

This set to 0 is a rough approximation.  Higher values, like 1, 2, 3 make truer representations.

= Syntax =

```python
1. set the quality to some positive integer
set ellipsoid_quality, int

1. for example, turn up the quality for rendering
set ellipsoid_quailty, 3
```

= See Also =
Ray, Surface_Quality
