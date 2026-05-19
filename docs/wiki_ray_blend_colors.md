# Ray blend colors

When ray_blend_colors is set, it knocks out the RGB component of the ray_blend_red, ray_blend_green, ray_blend_blue.  For example, without blending a rainbow picture looks like:

but if, before ray tracing we set,

```python
set ray_blend_colors, on
set ray_blend_red, 1.0
```

as you can see PyMOL has knocked out all red coloring,

The amount of the colored component left is:
(1.0 - (ray_blend_COLOR)) * original_color
