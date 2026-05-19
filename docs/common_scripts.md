# Common PyMOL Script Patterns

## Fetch, style, and export in one script

```python
cmd.fetch('1hpv', async_=0)
cmd.hide('everything', 'all')
cmd.show('cartoon', 'polymer.protein')
cmd.show('sticks', 'organic')
cmd.show('spheres', 'metals')
cmd.util.cbc('polymer.protein')   # color chains
cmd.color('yellow', 'organic')
cmd.bg_color('white')
cmd.zoom('all', buffer=2)
cmd.ray(1600, 1200)
cmd.png(os.path.join(output_dir, '1hpv.png'), dpi=300, ray=1)
print("Saved 1hpv.png")
```

## Highlight active site / binding pocket

```python
# Select and style binding site residues
cmd.select('site', 'byres (polymer.protein within 4 of organic)')
cmd.hide('everything', 'all')
cmd.show('surface', 'polymer.protein')
cmd.set('transparency', 0.4, 'polymer.protein')
cmd.show('sticks', 'site')
cmd.show('sticks', 'organic')
cmd.color('white', 'polymer.protein')
cmd.color('green', 'site and elem C')
cmd.color('yellow', 'organic and elem C')
cmd.util.cnc('all')   # color heteroatoms by element
cmd.zoom('organic', buffer=4)
```

## Export FASTA sequences for all chains

```python
fasta = cmd.get_fastastr('polymer.protein')
with open(os.path.join(output_dir, 'sequences.fasta'), 'w') as f:
    f.write(fasta)
print("FASTA saved.")
```

## Compare two structures side-by-side

```python
cmd.fetch('1abc', async_=0)
cmd.fetch('2xyz', async_=0)
result = cmd.super('2xyz', '1abc')
cmd.hide('everything', 'all')
cmd.show('cartoon', 'all')
cmd.color('cyan', '1abc')
cmd.color('salmon', '2xyz')
cmd.zoom('all')
print(f"RMSD: {result[0]:.3f} Å over {result[1]} atoms")
```

## Color by conservation (manual B-factor trick)

If you have conservation scores for each residue, store them in B-factor:
```python
conservation = {'1': 0.9, '2': 0.4, '15': 1.0, ...}  # resi -> score
stored.dummy = None
for resi, score in conservation.items():
    cmd.alter(f'polymer.protein and resi {resi}', f'b={score}')
cmd.spectrum('b', 'blue_white_red', 'polymer.protein', minimum=0, maximum=1)
```

## Create symmetry mates

```python
cmd.symexp('mates', '1abc', '1abc', 6.0)   # expand within 6 Å
cmd.color('grey', 'mates*')
cmd.show('cartoon', 'mates*')
```

## Morph/interpolate between two states (if multi-model PDB)

```python
cmd.load('multi.pdb', 'ensemble')   # loads all models as states
cmd.mplay()                          # play morph animation
cmd.set('defer_builds_mode', 0)      # ensure all states rendered
```

## Export session

```python
cmd.save(os.path.join(output_dir, 'session.pse'))   # PyMOL session file
# Reload with: cmd.load('session.pse')
```

## Iterate over all loaded objects

```python
for obj in cmd.get_object_list():
    n = cmd.count_atoms(obj)
    chains = cmd.get_chains(obj)
    print(f"  {obj}: {n} atoms, chains {chains}")
```

## Per-chain center of mass

```python
for chain in cmd.get_chains('polymer.protein'):
    stored.xyz = []
    cmd.iterate_state(1, f'polymer.protein and chain {chain} and name CA',
                      'stored.xyz.append((x,y,z))')
    if stored.xyz:
        cx = sum(p[0] for p in stored.xyz) / len(stored.xyz)
        cy = sum(p[1] for p in stored.xyz) / len(stored.xyz)
        cz = sum(p[2] for p in stored.xyz) / len(stored.xyz)
        print(f"  Chain {chain}: ({cx:.2f}, {cy:.2f}, {cz:.2f})")
```
