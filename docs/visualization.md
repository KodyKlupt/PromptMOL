# Visualization: Representations and Display

## Show and hide

```python
cmd.show('cartoon', 'polymer.protein')
cmd.show('sticks', 'organic')
cmd.show('surface', 'polymer.protein')
cmd.show('spheres', 'metals')
cmd.hide('everything', 'selection')
cmd.hide('cartoon', 'chain B')
```

Available representations:
- `cartoon` — secondary structure ribbons (most common for proteins)
- `sticks` — all bonds as sticks
- `lines` — thin wire bonds
- `spheres` — CPK/VDW spheres
- `surface` — molecular surface
- `mesh` — surface as wireframe mesh
- `ribbon` — simple ribbon (less detail than cartoon)
- `dots` — dot surface
- `nonbonded` — non-bonded atoms (ions, unconnected atoms)
- `nb_spheres` — nonbonded as spheres
- `licorice` — rounded sticks (like VMD)

## Common visualization setup patterns

```python
# Standard protein + ligand view
cmd.hide('everything', 'all')
cmd.show('cartoon', 'polymer.protein')
cmd.show('sticks', 'organic')
cmd.show('sticks', 'byres (polymer.protein within 4 of organic)')
cmd.show('spheres', 'metals')
cmd.show('nonbonded', 'solvent')

# Surface with hidden cartoon underneath
cmd.show('surface', 'polymer.protein')
cmd.set('transparency', 0.3, 'polymer.protein')

# Cartoon + sticks for whole structure
cmd.show('cartoon', 'all')
cmd.show('sticks', 'all')
cmd.hide('sticks', 'polymer.protein and not (name CA+N+C+O)')

# Highlight specific residues
cmd.show('sticks', 'resi 50+100+150')
cmd.show('spheres', 'resi 50+100+150 and name CA')
```

## Set transparency

```python
cmd.set('transparency', 0.5, 'selection')       # surface transparency (0=opaque)
cmd.set('cartoon_transparency', 0.5, 'selection') # cartoon transparency
cmd.set('stick_transparency', 0.3, 'selection')
```

## Zoom and orient

```python
cmd.zoom('selection')           # zoom to fit selection
cmd.zoom('all')                 # zoom to fit everything
cmd.orient('selection')         # orient to principal axes of selection
cmd.center('selection')         # center view on selection
cmd.reset()                     # reset view to default
```

## Object visibility

```python
cmd.enable('object_name')    # make object visible
cmd.disable('object_name')   # hide object (keeps it loaded)
cmd.enable('all')
cmd.disable('all')
```

## Labels

```python
cmd.label('selection and name CA', '"(%s%s)" % (resn, resi)')  # residue labels
cmd.label('selection', '"%.1f" % b')   # B-factor labels
cmd.hide('labels', 'all')              # remove all labels
cmd.set('label_size', 14)              # font size
cmd.set('label_color', 'white')
```
