# Data Collection: iterate, iterate_state, and stored

## The stored object

`stored` is a pre-defined namespace shared between Python and PyMOL's evaluator.
Use it to pass data in and out of `cmd.iterate()`. Never write `cmd.stored`.

```python
stored.data = []
cmd.iterate('selection', 'stored.data.append((chain, resi, resn, name, b, q, elem))')
```

## Available properties in iterate

| Property | Description |
|----------|-------------|
| `model`  | object name |
| `chain`  | chain ID |
| `resi`   | residue sequence number (string) |
| `resn`   | residue name (3-letter code) |
| `name`   | atom name (CA, N, O, etc.) |
| `elem`   | element symbol |
| `b`      | B-factor (temperature factor) |
| `q`      | occupancy |
| `formal_charge` | formal charge |
| `partial_charge` | partial charge |
| `oneletter` | one-letter amino acid code (protein only) |
| `ss`     | secondary structure (H=helix, S=sheet, L=loop) |
| `index`  | internal atom index |
| `rank`   | atom rank |

Note: `mass` is NOT available in open-source PyMOL iterate.
Note: `x`, `y`, `z` coordinates are only available in `iterate_state`.

## iterate_state — get coordinates

```python
stored.coords = []
cmd.iterate_state(1, 'polymer.protein and name CA',
                  'stored.coords.append((chain, resi, resn, x, y, z))')
```

The first argument is the state number (usually 1).

## Common data collection patterns

### Per-residue B-factors

```python
stored.rows = []
cmd.iterate('polymer.protein and name CA',
            'stored.rows.append((chain, resi, resn, b))')
with open(os.path.join(output_dir, 'bfactors.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['chain', 'resi', 'resn', 'b_factor'])
    w.writerows(stored.rows)
print(f"Saved {len(stored.rows)} residues to bfactors.csv")
```

### Sequence extraction

```python
fasta = cmd.get_fastastr('polymer.protein')
with open(os.path.join(output_dir, 'sequence.fasta'), 'w') as f:
    f.write(fasta)
```

### Residue composition

```python
stored.resns = []
cmd.iterate('polymer.protein and name CA', 'stored.resns.append(resn)')
from collections import Counter
counts = Counter(stored.resns)
for aa, n in sorted(counts.items()):
    print(f"  {aa}: {n}")
```

### Molecular weight (element-based — `mass` not available in open-source)

```python
ATOMIC_MASS = {
    'C': 12.011, 'N': 14.007, 'O': 15.999, 'S': 32.06,
    'H': 1.008,  'P': 30.974, 'F': 18.998, 'CL': 35.45,
    'BR': 79.904, 'I': 126.90, 'FE': 55.845, 'ZN': 65.38,
    'MG': 24.305, 'CA': 40.078, 'MN': 54.938,
}
stored.elems = []
cmd.iterate('polymer.protein', 'stored.elems.append(elem.upper())')
mw = sum(ATOMIC_MASS.get(e, 0) for e in stored.elems)
print(f"Approx MW: {mw:.1f} Da ({mw/1000:.2f} kDa)")
```

### Secondary structure content

```python
stored.ss = []
cmd.iterate('polymer.protein and name CA', 'stored.ss.append(ss)')
total = len(stored.ss)
helix = stored.ss.count('H')
sheet = stored.ss.count('S')
loop  = total - helix - sheet
print(f"Helix: {helix/total*100:.1f}%  Sheet: {sheet/total*100:.1f}%  Loop: {loop/total*100:.1f}%")
```

### Export all CA coordinates to CSV

```python
stored.rows = []
cmd.iterate_state(1, 'polymer.protein and name CA',
                  'stored.rows.append((model, chain, resi, resn, x, y, z))')
with open(os.path.join(output_dir, 'ca_coords.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['object', 'chain', 'resi', 'resn', 'x', 'y', 'z'])
    w.writerows(stored.rows)
print(f"Saved {len(stored.rows)} Cα atoms.")
```

### Ligand atom properties

```python
stored.lig = []
cmd.iterate('organic', 'stored.lig.append((name, elem, partial_charge, b))')
for name, elem, pq, b in stored.lig:
    print(f"  {name:4s} {elem:2s}  charge={pq:+.3f}  B={b:.2f}")
```
