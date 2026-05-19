# Cylinder shader ff workaround

- New in PyMOL 1.5.0*

- Removed in PyMOL 1.7.6 *

## OVERVIEW
When cylinders (as in stick representation) are drawn incorrectly, enabling this option might fix the problem. This
option is often required in NVIDIA's video cards (GeForce and Quadro).

Image:shader_bug.png| Incorrect rendering in GeForce GTX 580
Image:shader_bug_fixed.png| Setting this option 'on' fixed the problem

## USAGE
 set cylinder_shader_ff_workaround, on

The default is off.

Once you found this option necessary, you can add this to .pymolrc.
