# Ray orthoscopic

##  Overview
This setting controls whether ray-traced images are rendered with or without perspective.  Note that this can be in conflict with the setting "orthoscopic"; by default, images are rendered with the same orthoscopic setting as the viewport, unless "ray_orthoscopic" is deliberately set otherwise.

##  Settings
```python
set ray_orthoscopic, off   # render ray-traced images with perspective (2-4x SLOWER)
set ray_orthoscopic, on    # render ray-traced images without perspective
```

##  Examples
Image:orthoon2.png|orthoscopic on (perspective off)

Image:orthooff2.png |orthoscopic off (perspective on)
For many images, the difference is hardly visible.

Image:orthoon.png|orthoscopic on (perspective off)

Image:orthooff.png |orthoscopic off (perspective on)
Especially when straight features parallel to the z axis are shown, the effect may be large.
