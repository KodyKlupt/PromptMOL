# Rotate

- *rotate** can be used to rotate the atomic coordinates of a molecular object.  Behavior differs depending on whether or not the **object** parameter is specified.

If object is **None**, then rotate rotates the atomic coordinates according to the axes and angle for the selection and state provided.

If object is set to an object name, then selection and state are ignored and instead of translating the atomic coordinates, the object matrix is modified. This option is intended for use in animations.

The "camera" option controls whether the camera or the model's axes are used to interpret the translation vector.  To move the object relative to the camera set **camera=1** (which is default), or to move the molecule relative to the model's geometry, set **camera=0**.

If this doesn't do what you want, consider Turn.

### USAGE
```python
rotate axis, angle [,selection [,state [,camera [,object [,origin]]]]]
```

### ARGUMENTS
- *axis**
::x, y, z, or float vector: axis about which to rotate

- *angle**
::float: degrees of rotation

- *selection**
::    string: atoms whose coordinates should be modified {default: all}
- *state**
::    > 0: only the indicated state is modified
::    = 0: all states are modified
::    = -1: only the current state is modified {default}
- *camera**
::     = 0 or 1: is the axis specific in camera coordinates? {default: 1}
- *object**
::    string: object name (only if changing object matrix) {default: None}
- *origin**
::    float vector: origin of rotation {default: None}

### PYMOL API
```python
cmd.rotate(list-or-string axis, angle=0, string selection = "all", int state = 0,
           int camera = 1, string object = None)
```

### EXAMPLES
 rotate x, 45, pept
 rotate [1,1,1], 10, chain A

#### =Electrostatic Map Caveat=
If you have an electrostatic map and it's not rotating with the molecule as you expect it to, see the Turn command.  Turn moves the camera and thus the protein and map will be changed.

### SEE ALSO
object matrix Translate Turn Model_Space_and_Camera_Space
