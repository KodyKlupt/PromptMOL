# Defer builds mode

= Overview =
The defer_builds_mode setting for improved performance with long trajectories.  This now makes it possible to work with files containing thousands of states, and to render impossibly long movies piecewise.  This setting, as shown below, stops PyMOL caching the geometry of trajectory data in RAM.

= Usage =

```python
1. improve PyMOL performance for many-state objects and long movies.
set defer_builds_mode, 3
```

= See Also =
- Load_Traj
- async_builds
