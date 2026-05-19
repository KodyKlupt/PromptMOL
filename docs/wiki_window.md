# Window

- *window** controls the visibility of PyMOL's output window

Some actions (maximize, focus, defocus) are not consistent across operating systems.

- Non-functional in PyMOL 2.0, will be available again in 2.1*

##  Usage
 window [ action [, ... ]]

##  Actions
Hide the window (Warning: might make the window inaccessible. Intended for programmed automation):

 window hide

Show the window (reverse of **hide**):

 window show

Place the window at **x, y** screen coordinates:

 window position, x, y

Resize the window:

 window size, width, height

Place and resize in a single operation:

 window box, x, y, width, height

If any window corner is not on the visible screen, move the window and if necessary, resize (shrink) to screen dimensions:

 window fit

Maximize the window:

 window maximize

Give the OpenGL window focus:

 window focus

##  Example
Place in upper left corner and resize to 1000x500

 window box, 0, 0, 1000, 500
