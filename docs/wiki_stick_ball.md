# Stick ball

##  Overview
- *This setting is deprecated in v1.5 and later as it is always enabled.**

The setting "stick_ball" controls whether bonded atoms are shown simply as joined sticks (set stick_ball, off) or as traditional "ball-and-stick" representation (set stick_ball, on).  Note that simply setting stick_ball on will result in balls with the same radius as the sticks and so will appear only slightly different (the joins will be smoother).

##  Settings
```python
set stick_ball, on   # displays atoms as balls joined by sticks
set stick_ball, off  # displays only connected sticks

set stick_ball_ratio, 1.7 # change the radius of the balls
```

##  Examples
Open the images to actually see the details!

Image:stick_ball_off.png|stick_ball, off
Image:stick_ball_on.png|stick_ball, on
Image:Stick_ball_ratio_1.5.png|stick_ball "on" with stick_ball_ratio at 1.5
