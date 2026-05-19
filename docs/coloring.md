# Coloring in PyMOL

## Basic color by name

```python
cmd.color('slate', 'polymer.protein')
cmd.color('red', 'chain A')
cmd.color('cyan', 'chain B')
cmd.color('yellow', 'organic')
cmd.color('white', 'all')
```

Common named colors: red, green, blue, cyan, magenta, yellow, white, black, orange,
slate, wheat, salmon, limon, violet, tv_red, tv_green, tv_blue, tv_orange, tv_yellow,
marine, forest, firebrick, hotpink, lightblue, lightpink, lightteal, deepteal,
brightorange, splitpea, smudge, dirtyviolet, warmpink.

## Color by property (spectrum/gradient)

```python
# B-factor gradient (blue=low, red=high)
cmd.spectrum('b', 'blue_red', 'polymer.protein')

# B-factor with custom range
cmd.spectrum('b', 'blue_white_red', 'all', minimum=10, maximum=80)

# Rainbow by residue number
cmd.spectrum('resi', 'rainbow', 'polymer.protein')

# By chain
cmd.spectrum('chain', 'rainbow', 'all')

# By partial charge
cmd.spectrum('partial_charge', 'red_white_blue', 'organic')
```

Available spectrums: rainbow, blue_red, red_blue, blue_white_red, red_white_blue,
cyan_red, red_cyan, yellow_blue, green_red, rainbow2, rainbow_rev.

## Color by structure type

```python
cmd.util.cbc('all')          # color by chain (each chain unique color)
cmd.util.cbss('all')         # color by secondary structure (helix=red, sheet=yellow, loop=green)
cmd.util.cnc('all')          # color by name/element
cmd.util.cbag('all')         # color by element (C=green, N=blue, O=red, S=yellow)
cmd.util.cbac('all')         # color C atoms only (leave heteroatoms colored by element)
```

## Element-specific coloring (CPK scheme)

```python
cmd.color('white', 'polymer.protein and elem C')
cmd.color('blue', 'polymer.protein and elem N')
cmd.color('red', 'polymer.protein and elem O')
cmd.color('yellow', 'polymer.protein and elem S')
# Ligand carbons in different color
cmd.color('green', 'organic and elem C')
```

## Set custom RGB color

```python
cmd.set_color('mycolor', [0.8, 0.2, 0.5])   # RGB values 0–1
cmd.color('mycolor', 'selection')
```

## Color by B-factor — detailed patterns

```python
# Continuous blue (low) → red (high) gradient
cmd.spectrum('b', 'blue_white_red', 'polymer.protein and name CA')

# Map surface color to B-factor
cmd.show('surface', 'polymer.protein')
cmd.spectrum('b', 'blue_red', 'polymer.protein')

# Custom color scale using iterate
stored.bvals = []
cmd.iterate('polymer.protein and name CA', 'stored.bvals.append(b)')
b_min, b_max = min(stored.bvals), max(stored.bvals)
cmd.spectrum('b', 'blue_red', 'polymer.protein and name CA',
             minimum=b_min, maximum=b_max)
```

## Color by RMSD after alignment

After `cmd.super()` or `cmd.align()`, use the object's Q-score/RMSD per atom
stored in B-factor with `cmd.spectrum('b', ...)`.
