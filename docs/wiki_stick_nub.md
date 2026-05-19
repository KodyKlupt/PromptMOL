# Stick nub

## Overview
The stick_nub setting controls the height of the cones at the end of the sticks in stick representation.  This only affects the simple representation: this setting doesn't have any effect for ray tracing.

Image:Sticknub default.png|Default stick_nub setting.
Image:Sticknub 0.png|Stubby nubs--stick nub set to 0.
Image:Sticknub 2.png|Nub spears: stick_nub=2.0

## Syntax
```python
set stick_nub, *float*
```

Where *float* is a floating point number.  The default value is 0.7.
## Example
```python
set stick_nub, 0
```
