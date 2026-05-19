# Half bonds

## Overview
The half_bonds setting determines whether a half bond will be drawn between visible and hidden atoms.

{|
|-
| valign="top"|

| valign="top"|

|-
|}

## Syntax
set half_bonds, *boolean*

Where *boolean* may be one of:

0  0.0  off  false

or:

1  1.0  on  true

## Example
To turn on half bonds:

```python
set half_bonds, 1
```

To turn off half bonds (default):

```python
set half_bonds, off
```
