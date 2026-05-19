# Cartoon putty transform

= Overview =
This setting determines how PyMOL renders the transformation of original values into putty related settings.

= Usage =

```python
1. normalized nonlinear scaling
set cartoon_putty_transform, 0
1. relative nonlinear scaling
set cartoon_putty_transform, 1
1. scaled nonlinear scaling
set cartoon_putty_transform, 2
1. absolute nonlinear scaling
set cartoon_putty_transform, 3

1. normalized linear scaling
set cartoon_putty_transform, 4
1. relative linear scaling
set cartoon_putty_transform, 5
1. scaled linear scaling
set cartoon_putty_transform, 6
1. absolute linear scaling from the B factor
set cartoon_putty_transform, 7

1. implied RMS scaling
set cartoon_putty_transform, 8
```

= See Also =
- putty
- Cartoon_putty_scale_max
- Cartoon_putty_scale_min
