# Light count

##  Overview
set light_count defines the number of light sources.
Setting to 0 or 1 removes any directional light source resulting in no shadows. Light_count does affect ambient lighting.

##  Syntax
```python
set light_count,                           #default 2
```

## PyMol API
```python
cmd.set(light_count,int sources)
```

##  Example
Image:light_count_0.png|light_count 0
Image:light_count_2.png|light_count 2 (default)
Image:light_count_10.png|light_count 10

=See Also=
Light
