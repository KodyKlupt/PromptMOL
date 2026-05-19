# Backface cull

## Overview
- *backface_cull** controls whether or not backward facing triangles are not filtered out when ray tracing.

## Syntax
```python
1. on; default
set backface_cull, 1

1. off; allows the visualization of the "other side" (inside) of a surface
set backface_cull, 0
```

- *Note**: To allow or disallow visualization of the inside of a surface, see two_sided_lighting.

## Examples
Image:Cull_backface_on.jpg|cull_backface ON
Image:Cull_backface_off.jpg|cull_backface OFF
