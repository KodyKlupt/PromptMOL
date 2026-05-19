# Stick ball ratio

##  Overview
The setting "stick_ball_ratio" controls the relative ratio between the radius of sticks connecting bonded atoms and the radius of the atom spheres.  Note that simply setting "stick_ball, on" will result in balls with the same radius as the sticks and so will appear only slightly different (the joins will be smoother).  Changing the stick_ball_ratio without setting "stick_ball, on" will -- obviously -- have no apparent effect.

##  Settings
```python
set stick_ball_ratio, 1.5
```

##  Related
```python
set stick_ball, on   # displays atoms as balls joined by sticks
set stick_ball, off  # displays only connected sticks
```

##  Examples
Open the images to actually see the details!

Image:stick_ball_off.png|stick_ball, off
Image:stick_ball_on.png|stick_ball, on
Image:Stick_ball_ratio_1.5.png|stick_ball "on" with stick_ball_ratio at 1.5
