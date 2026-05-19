# Rendering and Image Export

## Basic PNG export (no ray tracing)

```python
cmd.png(os.path.join(output_dir, 'fig.png'), width=1920, height=1080, dpi=150)
```

## Ray-traced high-quality PNG

```python
cmd.bg_color('white')
cmd.set('antialias', 2)
cmd.set('ray_opaque_background', 1)
cmd.ray(2400, 1800)
cmd.png(os.path.join(output_dir, 'fig.png'), width=2400, height=1800, dpi=300, ray=1)
```

## Ray trace modes

```python
cmd.set('ray_trace_mode', 0)   # standard (default)
cmd.set('ray_trace_mode', 1)   # standard + black outline (publication style)
cmd.set('ray_trace_mode', 2)   # line art (cartoon outlines)
cmd.set('ray_trace_mode', 3)   # toon / cel-shading
```

## Lighting settings

```python
cmd.set('ambient', 0.4)           # ambient light (0-1, default ~0.2)
cmd.set('direct', 0.7)            # direct light intensity
cmd.set('reflect', 0.5)           # specular reflection
cmd.set('ray_shadows', 1)         # enable shadows (1=on, 0=off)
cmd.set('shininess', 50)          # surface shininess
cmd.set('specular', 0.5)
```

## Background color

```python
cmd.bg_color('white')
cmd.bg_color('black')
cmd.bg_color('grey')
```

## Depth cueing / fog

```python
cmd.set('depth_cue', 1)       # enable depth cueing
cmd.set('fog_start', 0.45)    # fog start distance
cmd.set('ray_depth_cue', 1)   # depth cue in ray tracing
```

## Cartoon settings (fancy rendering)

```python
cmd.set('cartoon_fancy_helices', 1)    # ribbon-style helices
cmd.set('cartoon_fancy_sheets', 1)     # arrow-style strands
cmd.set('cartoon_tube_radius', 0.5)    # loop tube radius
cmd.set('cartoon_helix_radius', 1.0)   # helix cylinder radius
cmd.set('cartoon_loop_quality', 10)    # loop smoothness
```

## Stick settings

```python
cmd.set('stick_radius', 0.2)        # thicker sticks
cmd.set('stick_ball', 1)            # ball-and-stick style
cmd.set('stick_ball_ratio', 1.5)    # ball size relative to stick
```

## Sphere settings

```python
cmd.set('sphere_scale', 0.5, 'all')          # VDW sphere scale
cmd.set('sphere_scale', 1.0, 'metals')       # full VDW for metals
```

## Full publication-quality workflow

```python
cmd.bg_color('white')
cmd.set('ray_trace_mode', 1)
cmd.set('antialias', 2)
cmd.set('ray_opaque_background', 1)
cmd.set('ambient', 0.35)
cmd.set('direct', 0.7)
cmd.set('ray_shadows', 1)
cmd.set('cartoon_fancy_helices', 1)
cmd.set('cartoon_fancy_sheets', 1)
cmd.zoom('all', buffer=2)
cmd.ray(3000, 2000)
cmd.png(os.path.join(output_dir, 'publication.png'), dpi=300, ray=1)
print("Saved publication.png")
```
