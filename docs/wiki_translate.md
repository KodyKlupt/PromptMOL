# Translate

- *translate** can be used to translate the atomic coordinates of a molecular object (move an object).  Behavior differs depending on whether or not the "object" parameter is specified.

If object is None, then translate translates atomic coordinates according to the vector provided for the selection and in the state provided.

If object is set to an object name, then selection and state are ignored and instead of translating the atomic coordinates, the object matrix is modified. This option is intended for use in animations.

The "camera" option controls whether the camera or the model's axes are used to interpret the translation vector.  To move the object relative to the camera set **camera=1** (which is default), or to move the molecule relative to the model's geometry, set, **camera=0**.

### USAGE
```python
translate vector [,selection [,state [,camera [,object ]]]]
```

### ARGUMENTS
- *vector**
::float vector: [x, y, z] translation vector

- *selection**
::    string: atoms whose coordinates should be modified {default: all}

- *state**
::    state > 0: only the indicated state is modified
::    state = 0: all states are modified
::    state = -1: only current state is modified {default}

- *camera**
::    0 or 1: is the vector in camera coordinates? {default: 1 (yes)}

- *object**
::    string: object name (only if rotating object matrix) {default: None}

### PYMOL API
```python
cmd.translate(list vector, string selection = "all", int state = 0,
              int camera = 1, string object = None)
```

### EXAMPLES
#### Example 1
A simple example; just move the alpha-carbons one Ang. along the X-axis.

```python
1. move the alpha carbons one Ang. on the X-axis
translate [1,0,0], name ca
```

#### Example 2
A slightly more complicated example.  Load two proteins, align them, and then move one away from the other to see their similarities separately.

```python
1. load 1cll and 1ggz
fetch 1cll 1ggz, async=0

1. align the two proteins
cealign 1cll, 1ggz

1. orient the proteins
orient

1. move 1cll above 1ggz so we can
1. see both proteins separately
translate [0, 40, 0], 1cll
```

### NOTES
1. if state = 0, then only visible state(s) are affected.
1. if state = -1, then all states are affected.

### SEE ALSO
Rotate, Move, Model_Space_and_Camera_Space
