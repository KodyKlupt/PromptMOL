# Mpng

- *mpng** writes a series of numbered movie frames to png files with the specified prefix.  If the **ray_trace_frames** variable is non-zero, these frames will be ray-traced.  This operation can take several hours for a long movie.

Be sure to disable **cache_frames** when issuing this operation on a long movie (>100 frames) to avoid running out of memory.

##  Usage
 mpng prefix [, first [, last [, preserve [, modal [, mode [, quiet
     [, width [, height ]]]]]]]]

Options "first" and "last" can be used to specify an inclusive interval over which to render frames.  Thus, you can write a smart Python program that will automatically distribute rendering over a cluster of workstations.  If these options are left at zero, then the entire movie will be rendered.

##  Arguments
- **prefix** = string: filename prefix for saved images -- output files will be numbered and end in ".png"
- **first** = integer: starting frame {default: 0 (first frame)}
- **last** = integer: last frame {default: 0 (last frame)}
- **preserve** = 0/1: Only write non-existing files {default: 0}
- **modal** = integer: will frames be rendered with a modal draw loop
- **mode** = int: 2=ray, 1=draw, 0=normal {default: -1, check ray_trace_frames or draw_frames}
- **width** = int: width in pixels {default: current viewport}
- **height** = int: height in pixels {default: current viewport}

##  Python API
```python
cmd.mpng(str prefix, int first=0, int last=0, int preserve=0,
    int modal=0, int mode=-1, int quiet=1,
    int width=0, int height=0)
```
