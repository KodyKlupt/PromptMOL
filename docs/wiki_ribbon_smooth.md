# Ribbon smooth

## Overview
This PyMOL setting determines smoothly how PyMOL draws ribbons.  Turning *on* the setting smooths out the ribbons and make the image look cleaner.  The setting is by default **off**, and yet, when turned **on** shows absolutely no decreased performance.

## Usage
```python
1. show ribbons, first
hide; show ribbon

1. turn on smoothing
set ribbon_smooth, 1

1. turn off smoothing
set ribbon_smooth, 0
```
