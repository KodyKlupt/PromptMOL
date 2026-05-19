# Light

= Overview =
Lighting is important for high-quality shots. PyMOL supports of up to 10 virtual lights.  You can turn the lights on/off and also position them where you want (behind the camera).

Light2..Light9 control where the other lights go.

Image:L1.png|Normal lighting
Image:L2.png|Light1 moved a bit.  Notice how the shadows have changed.

= Syntax =

```python
1. set the light to some position.  The 'position'
1. must be a vector specifying the XYZ location
1. to put the light.
set light, position

1. for example
set light, [ -0.55, -0.70, 0.15 ]
```

= User Hint =

Image:Ll.gif|Moving lights make for a cool effect; you can make this look better by smoothing out the distances and ranges.
:
One neat trick, for rendering a "sunset" on your protein is to turn off all the lights, then render the scene as you move the light across the scene.  The shadows move across the protein based on the light position and it looks like the sun is setting.

##  The Code
Here's the code for the animated GIF shown above.

```python
python
cmd.set("light", ll)
for x in range(10):
        l = [ -0.4 + 2*float(x/10.), -0.4, -1  ]
        print l
        cmd.set("light", l)
        cmd.ray()
        cmd.png("lll" + str(x) + ".png" )
for x in range(10):
        l[0] -= 2*float(x/10.)
        print l
        cmd.set("light", l)
        cmd.ray()
        cmd.png("llll" + str(x) + ".png" )
python end
```

Then, in the shell do

```
convert lll* llll* light_movie.gif
```

= See Also =
Ray
