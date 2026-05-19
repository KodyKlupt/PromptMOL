# Ray trace gain

= Overview =
When ray tracing, PyMOL knows the Z-depth of coordinates.  The ray_trace_gain setting darkens pixels based on their Z-depth.

Image:Ray trace gain0.png|ray_trace_gain,0
Image:Ray trace gain2.png|ray_trace_gain,2
Image:Ray trace gain8.png|ray_trace_gain,8
Image:Ray trace gain20.png|ray_trace_gain,20

= Syntax =

```python
1. set it
set ray_trace_gain, 7

1. you need to ray trace the image to see it
ray
```

= See Also =
ray
