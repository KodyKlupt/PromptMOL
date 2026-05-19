# PyMOL Selection Language

## Basic keywords

```
all           — every atom
none          — empty selection
polymer       — all polymer atoms (protein + nucleic)
polymer.protein  — protein only
polymer.nucleic  — DNA/RNA only
organic       — small molecule ligands (HETATM, non-solvent)
solvent       — water molecules
metals        — metal ions
hetatm        — all non-standard residues (includes ligand + solvent + metals)
```

## Chain, residue, atom filters

```
chain A                  — chain A
chain A+B                — chains A and B
resi 50                  — residue 50
resi 50-100              — residues 50 through 100
resi 10+20+30            — specific residues
resn ALA                 — alanine residues
resn LIG                 — residue named LIG (typical ligand name)
name CA                  — alpha carbon atoms only
name CA+CB+N+C+O         — backbone + beta carbon
elem C                   — carbon atoms
elem S                   — sulfur atoms
b > 50                   — atoms with B-factor above 50
q < 0.5                  — partial occupancy atoms
```

## Secondary structure

```
ss h          — helix atoms
ss s          — sheet (strand) atoms
ss l          — loop atoms (everything else)
```

## Spatial selections

`within` always requires `of <target>`:

```python
# Correct — residues within 5 Å of organic ligand
'byres (organic expand 5)'
'byres (polymer.protein within 5 of organic)'

# Correct — atoms within 4 Å of ligand
'polymer.protein within 4 of organic'

# WRONG — crashes:
'within 5 of organic'       # missing selection before 'within'
'byres (organic within 5)'  # missing "of target"
```

## Boolean operators

```
sele1 and sele2    — intersection
sele1 or sele2     — union
not sele1          — complement
sele1 and not sele2
```

## Useful expansion operators

```
byres (selection)       — expand to whole residues
bymolecule (selection)  — expand to whole molecules/chains
bychain (selection)     — expand to chains
expand N, selection     — expand by N angstroms
```

## Practical examples

```python
# Active site residues near a ligand
cmd.select('active_site', 'byres (polymer.protein within 4 of organic)')

# Surface-exposed residues (use with solvent access calculations)
cmd.select('exposed', 'polymer.protein and not (byres (polymer.protein within 3.5 of solvent))')

# All cysteines in chain A
cmd.select('cys_A', 'resn CYS and chain A')

# Backbone atoms only
cmd.select('backbone', 'polymer.protein and name N+CA+C+O')

# Catalytic triad (Ser-His-Asp) example
cmd.select('triad', 'resn SER+HIS+ASP and polymer.protein')
```
