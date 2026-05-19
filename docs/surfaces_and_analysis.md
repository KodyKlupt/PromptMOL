# Surfaces, Electrostatics, and Structural Analysis

## Molecular surface

```python
# Show surface for protein
cmd.show('surface', 'polymer.protein')
cmd.set('transparency', 0.3, 'polymer.protein')   # semi-transparent

# Surface colored by hydrophobicity (approximate via residue color)
cmd.show('surface', 'polymer.protein')
cmd.util.cbag('polymer.protein')   # color by atom type
```

## Electrostatic surface (APBS / built-in)

Open-source PyMOL doesn't include APBS natively. Use the plugin menu.
For a simple charge-based coloring approximation:

```python
# Color by partial charge (if charges assigned)
cmd.show('surface', 'polymer.protein')
cmd.spectrum('partial_charge', 'red_white_blue', 'polymer.protein')
```

## Solvent-accessible surface area

PyMOL doesn't compute SASA directly via `cmd`. Use `get_area`:

```python
sasa = cmd.get_area('polymer.protein', load_b=0)   # SASA in Å²
print(f"SASA: {sasa:.1f} Å²")

# Per-residue SASA via load_b (stores SASA in B-factor)
cmd.get_area('polymer.protein', load_b=1)
# Now B-factors contain per-atom SASA contributions
stored.sasa = []
cmd.iterate('polymer.protein and name CA', 'stored.sasa.append((chain, resi, resn, b))')
```

## Cavity / pocket detection

PyMOL can show cavities using surface + cavity mode:

```python
cmd.show('surface', 'polymer.protein')
cmd.set('surface_cavity_mode', 1)   # show only pockets/cavities
cmd.set('surface_cavity_radius', 3)  # minimum pocket radius
```

## Mesh representation

```python
cmd.show('mesh', 'polymer.protein')
cmd.set('mesh_width', 0.5)
cmd.color('marine', 'polymer.protein')
```

## RMSD calculation between two selections

```python
# After super/align, RMSD is returned directly
result = cmd.super('mobile', 'target')
print(f"RMSD: {result[0]:.3f} Å, {result[1]} atoms")

# Between current positions (no alignment)
rmsd = cmd.rms_cur('mobile and name CA', 'target and name CA', matchmaker=-1)
print(f"Cα RMSD (no fitting): {rmsd:.3f} Å")
```

## Principal component / moments of inertia

```python
# Get center of mass via iterate_state
stored.xyz = []
cmd.iterate_state(1, 'polymer.protein', 'stored.xyz.append((x, y, z))')
n = len(stored.xyz)
cx = sum(p[0] for p in stored.xyz) / n
cy = sum(p[1] for p in stored.xyz) / n
cz = sum(p[2] for p in stored.xyz) / n
print(f"Centroid: ({cx:.2f}, {cy:.2f}, {cz:.2f})")
```

## Count residues by chain

```python
stored.chains = {}
cmd.iterate('polymer.protein and name CA',
    'stored.chains.setdefault(chain, []).append(resn)')
for chain in sorted(stored.chains):
    print(f"  Chain {chain}: {len(stored.chains[chain])} residues")
```

## Identify disulfide bonds (CYS pairs within 2.1 Å)

```python
cmd.select('cys_sg', 'resn CYS and name SG')
n_cys = cmd.count_atoms('cys_sg')
print(f"Found {n_cys} Cys Sγ atoms")
cmd.distance('ss_bonds', 'cys_sg', 'cys_sg', cutoff=2.1, mode=0)
```

## Ramachandran-like phi/psi collection

```python
# phi/psi require 4-atom dihedral — not directly available in iterate
# Use cmd.phi_psi() if available in your PyMOL build:
phi_psi = cmd.phi_psi('polymer.protein')
# Returns dict keyed by (model, chain, resi) -> (phi, psi)
for key, (phi, psi) in list(phi_psi.items())[:10]:
    print(f"  {key}: phi={phi:.1f}° psi={psi:.1f}°")
```
