# Cgo transparency

This is an object-level setting to control transparency of Compiled Graphics Objects.

Usage:

```python
1. PyMOL command
set cgo_transparency, value [, object]

1. Python API
cmd.set("cgo_transparency", value [, object])
```

Arguments
- value (float) number between 0 and 1 (with 0 meaning the object is opaque, and 1 == invisible).
- object (str) name of the object to which to apply the setting (default: all CGO objects)
