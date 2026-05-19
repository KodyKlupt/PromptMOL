# Label size

##  Overview
Sets how large the labels are rendered. You can use positive numbers 2, 3, 4, etc for point sizes, or negative numbers for Angstrom-based sizes. Default is 14 points. Labels in Angstrom-size scale with the distance from the front plane, labels in point-size don't. This automatic scaling works with the draw command but not with the ray command.

##  Syntax
```python
1. set the label size to 10pt
set label_size, 10

1. set the label size to 1.5 Ang. -- large!
set label_size, -1.5
```
