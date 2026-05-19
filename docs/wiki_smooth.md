# Smooth

Smooth performs a window average of coordinate states.

= Usage =

```python
smooth [ selection [, passes [, window [, first [, last [, ends]]]]]]

1. for example, smooth and object with 30 passes and
1. a window size of 100.
smooth myObj, 30, 100
```


- ends = 0 or 1: controls whether or not the end states are also smoothed using a weighted asymmetric window

To see smooth in context see this example

= NOTES =
- This type of averaging is often used to suppress high-frequency vibrations in a molecular dynamics trajectory.
- This function is not memory efficient.  For reasons of flexibility, it uses two additional copies of every atomic coordinate for the calculation.  If you are memory-constrained in visualizing MD trajectories, then you may want to use an external tool such as ptraj to perform smoothing before loading coordinates into PyMOL.

= See Also =
Load_Traj, protect.
