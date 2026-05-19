# Measurements: Distances, Angles, Contacts

## Distance between two atoms

`get_distance()` requires EXACTLY 1 atom per selection — use full qualifiers.

```python
# Safe pattern — fully qualified selections
chain = cmd.get_chains('1hpv')[0]
dist = cmd.get_distance(
    f'1hpv and chain {chain} and resi 10 and name CA',
    f'1hpv and chain {chain} and resi 50 and name CA'
)
print(f"Distance: {dist:.2f} Å")

# Draw a distance object (visible dashed line)
cmd.distance('d1', 'resi 10 and name CA', 'resi 50 and name CA')
cmd.hide('labels', 'd1')   # hide numeric label if desired
```

Never use `get_distance('sele1', 'sele2')` without verifying each selection
resolves to exactly one atom — use chain, resi, name, and object all together.

## Angle between three atoms

```python
cmd.angle('ang1', 'atom1_sele', 'atom2_sele', 'atom3_sele')
```

## Dihedral angle (torsion)

```python
cmd.dihedral('dih1', 'atom1', 'atom2', 'atom3', 'atom4')
```

## Count atoms in a selection

```python
n = cmd.count_atoms('polymer.protein')
n_lig = cmd.count_atoms('organic')
print(f"Protein atoms: {n}, ligand atoms: {n_lig}")
```

## Hydrogen bonds

```python
cmd.find_pairs('sele1', 'sele2', mode=1, cutoff=3.5, angle=55)
# Returns list of ((obj1,idx1),(obj2,idx2)) pairs

# Alternative: distance-based H-bond visualization
cmd.dist('hbonds', 'donor_sele', 'acceptor_sele', mode=2, cutoff=3.5)
```

## Contacts (within distance)

```python
# Select all protein residues within 4 Å of ligand
cmd.select('contacts', 'byres (polymer.protein within 4 of organic)')

# Count them
n_contacts = cmd.count_atoms('contacts and name CA')
print(f"Contacting residues: {n_contacts}")

# Collect residue list
stored.contacts = []
cmd.iterate('contacts and name CA', 'stored.contacts.append((chain, resi, resn))')
for chain, resi, resn in sorted(stored.contacts):
    print(f"  {resn}{resi} chain {chain}")
```

## Pairwise distances between residues

```python
import csv
stored.pairs = []
# Get CA coordinates for two sets
cmd.iterate_state(1, 'chain A and name CA', 'stored.pairs.append((chain, resi, resn, x, y, z))')
# Then compute manually with math.sqrt
rows = stored.pairs
with open(os.path.join(output_dir, 'distances.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['chain1','resi1','resn1','chain2','resi2','resn2','dist_A'])
    for i, (c1,r1,n1,x1,y1,z1) in enumerate(rows):
        for c2,r2,n2,x2,y2,z2 in rows[i+1:]:
            d = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            if d < 10.0:
                w.writerow([c1,r1,n1,c2,r2,n2,f'{d:.2f}'])
print("Pairwise distances saved.")
```

## B-factor (temperature factor) statistics

```python
stored.bvals = []
cmd.iterate('polymer.protein and name CA', 'stored.bvals.append(b)')
bmin = min(stored.bvals)
bmax = max(stored.bvals)
bmean = sum(stored.bvals) / len(stored.bvals)
print(f"B-factor: min={bmin:.2f}, max={bmax:.2f}, mean={bmean:.2f}")
```
