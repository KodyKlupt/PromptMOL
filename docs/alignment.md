# Structure Alignment in PyMOL

## Super (recommended — structure-based)

```python
rmsd = cmd.super('mobile', 'target')
# Returns RMSD; aligns by structure similarity, robust for low sequence identity

# Align specific chains
rmsd = cmd.super('mobile and chain A', 'target and chain A')

# Align Cα only
rmsd = cmd.super('mobile and name CA', 'target and name CA')
```

`cmd.super()` is preferred over `cmd.align()` for most cases, especially when
sequence identity is below 30%.

## Align (sequence-guided)

```python
result = cmd.align('mobile', 'target')
# result = (RMSD, n_atoms, n_cycles, ...)
rmsd = result[0]
n_aligned = result[1]
print(f"RMSD: {rmsd:.2f} Å over {n_aligned} atoms")
```

## CE-align (combinatorial extension algorithm)

```python
cmd.cealign('target', 'mobile')   # note: target first, mobile second (reversed!)
```

CE-align is good for structurally distant proteins.

## Fit (no rejection — rigid body)

```python
cmd.fit('mobile', 'target')        # no outlier rejection, minimizes RMSD directly
```

## After alignment: coloring and display

```python
# Show both structures as cartoons
cmd.show('cartoon', 'all')

# Color differently
cmd.color('cyan', 'mobile')
cmd.color('salmon', 'target')

# Show superposition in one viewport
cmd.zoom('all')
```

## Compute RMSD without moving atoms

```python
rmsd = cmd.rms_cur('mobile', 'target')   # current positions, no alignment
rmsd = cmd.rms('mobile', 'target')       # with alignment but no movement
```

## Aligning multiple structures to a reference

```python
reference = '1abc'
for name in cmd.get_object_list():
    if name != reference:
        cmd.super(name, reference)
```

## Fetch and align two structures from RCSB

```python
cmd.fetch('1abc')
cmd.fetch('2xyz')
result = cmd.super('2xyz', '1abc')
rmsd = result[0]
cmd.hide('everything', 'all')
cmd.show('cartoon', 'all')
cmd.color('cyan', '1abc')
cmd.color('salmon', '2xyz')
cmd.zoom('all')
print(f"RMSD: {rmsd:.3f} Å")
```
