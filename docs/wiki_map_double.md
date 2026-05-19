# Map double

- *map_double** resamples a map at twice the current resolution.  The amount of memory required to store the map will increase eight-fold.

Image:Map_normal.png|Std. map mesh spacing
Image:Map_double.png|Map doubled
Image:Map_double2.png|Map double, doubled
Image:Map_double3.png|Map double, double, doubled

=Usage=

```python
map_double map_name [, state ]
```

= Example =

 fetch 1rx1
 fetch 1rx1, type=2fofc
 map_double 1rx1_2fofc
 isomesh mesh, 1rx1_2fofc
