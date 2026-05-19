# Pse export version

The pse_export_version setting switches to a legacy format when saving PSEs, so far possible. The value is the floating point number representation of the targeted legacy PyMOL version, for example **1.74** to save a session for PyMOL 1.7.4.

- New in PyMOL 1.7.6*

Session file loading is always backwards compatible, so any newer version of PyMOL can load old session files.

##  Examples
```python
1. current version (default)
set pse_export_version, 0
save current.pse

1. compatible with PyMOL 1.7.4
set pse_export_version, 1.74
save 174compat.pse
```

##  Known Limitations
The following objects are not or only partly supported:

- scenes before 1.7.6 (support added in 1.8.4)
- volumes before 1.7.2
- ramps
- CGOs
