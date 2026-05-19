# Get session

Returns a dictionary representation the currently loaded PyMOL session.The session file (.pse) is a compressed version of its output.

By using this API, user scripts can access many interesting properties which are otherwise inaccessible. Examples include Pymol2glmol and get_raw_distances scripts.

WARNING: This API is undocumented API, intended for internal use. Use it only when it is necessary.

##  Usage
```python
dict cmd.get_session(names='', partial=0)
```

##  Return value
The returned dictionary has following key-value pairs.
Some entries are missing if using *partial=1*.

- **main**: An array encoding window size. For example, [640, 480]
- **color_ext**:
- **settings**: An array of PyMOL's global settings. They are dumped by SettingAsPyList in layer1/Setting.c. Further details will not be discussed because scripts can access these values from cmd.get API.
- **colors**: If you have defined color names by Set Color, they are described here. Default color names (red, blue, etc...) will not appear. This dict can also be obtained by cmd.get_color_indices(). To get RGB definition of a color, get its pallet ID by cmd.get_color_index and convert it to RGB tuple by cmd.get_color_tuple.
- **view**: Same as cmd.get_view()
- **version**: Version number of PyMOL
- **view_dict**:
- **names**: This is the most complex but interesting part. Produced by ExecutiveGetNamedEntries, this array describes internal C-objects of the current session. Each element is an array of seven elements.

(documentation in progress... Please feel free to expand)

##  Examples
###  Object array
```python
x = cmd.get_session('myobj', 1)['names'][0]
x = [
    str name ('myobj'),
    int 0=object/1=selection,
    int enabled,
    list representations,
    int object_type,
    list object_data,
    str group_name,
]
```

###  Internals of a map object
The map data as a numpy array:

```python
import numpy
from pymol import cmd

cmd.map_new('mymap', 'gaussian', 0.5)

mymap = cmd.get_session('mymap', 1)['names'][0]
field_data = mymap[5][2][0][14][2]

values = numpy.reshape(field_data[6], field_data[4])
```

The dumped map datastructure:

```python
mymap[5][2][0] = [
    int Active,
    list Symmetry (like cmd.get_symmetry),
    list Origin,
    list Range (ExtentMax - ExtentMin),
    list Dim (?),
    list Grid (grid spacing),
    list Corner,
    list ExtentMin,
    list ExtentMax,
    int MapSource (?, 4),
    list Div (?, Dim - 1),
    list Min (?),
    list Max (?, ncells),
    list FDim (?, (ncells + 1) + [3]),
    [
        list field->dimensions (FDim[:3]),
        int field->save_points (?, 1),
        [# field->data
            int type (?, 0),
            int n_dim,
            int base_size (?, 4),
            int size (?, len * 4),
            list dim,
            list stride,
            list data,
        ],
        [# field->points
            ...
        ]
    ],
    [None],
]
```
