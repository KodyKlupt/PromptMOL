# Load traj

- *load_traj** loads a trajectory as "states" into an already loaded molecular object.

Since version 1.0, PyMOL uses the Molfile Plugin backend, which supports a variety of trajectory file formats. Older versions only supported the ascii AMBER format (".trj" file extension).

Loading a large trajectory may take up a lot of RAM, unless the defer_builds_mode is set to 3.

##  Usage
```python
load_traj filename [,object [,state [,format [,interval [,average ]
                   [,start [,stop [,max [,selection [,image [,shift
                   [, plugin ]
                   ]]]]]]]]]
```

##  Arguments
- **filename** = str: trajectory file path
- **object** = str: name of the molecular object where the trajectory should be appended as states {default: guess from filename}
- **state** = int: object state where to start appending states. To discard the currently loaded coordinates, use *state=1*. To append new states, use *state=0* {default: 0}
- **format** = str: specify file type instead of guessing from file extension (only affects AMBER .trj format, use "plugin" argument for Molfile Plugin types) {default: }

##  Examples
```python
1. topology from PDB file, trajectory from DCD file
load      sampletrajectory.pdb
load_traj sampletrajectory.dcd

1. gromacs trajectory, using "mytraj" as object name
load      sampletrajectory.gro, mytraj
load_traj sampletrajectory.xtc, mytraj

1. desmond trajectory
load      sample-out.cms, mytraj
load_traj sample_trj/clickme.dtr, mytraj

1. playing through states, memory optimized (but eventually slower)
set defer_builds_mode, 3
mplay
```
