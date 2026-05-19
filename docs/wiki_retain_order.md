# Retain order

The retain_order setting keeps atoms in the original order, instead of sorting them by atom identifiers. The "original order" is defined by the rank property, so technically with **retain_order=on**, PyMOL performs a rank-assisted sort.

Setting **retain_order** *on* or *off* triggers resorting of atoms.

##  File Format Specifics
- **vdb**: Since PyMOL 1.8.6, **retain_order** is automatically set for VIPERdb files, because they don't have unique chain identifiers
- **cif**: When **retain_order=on**, then PyMOL will skip loading of missing residues, because it depends on sorting

##  Syntax
```python
set retain_order,[0,1]
```

##  Example
Original PDB:

```
ATOM      1  CH3 ACE A   1      33.160  24.100  12.400  1.00  0.00
ATOM      2 HH31 ACE A   1      32.860  24.830  11.650  1.00  0.00
ATOM      3 HH32 ACE A   1      33.800  23.390  11.880  1.00  0.00
ATOM      4 HH33 ACE A   1      32.250  23.650  12.770  1.00  0.00
ATOM      5  C   ACE A   1      33.910  24.800  13.510  1.00  0.00
ATOM      6  O   ACE A   1      33.760  24.560  14.700  1.00  0.00
```

Loaded and exported with retain_order set to 0

```
ATOM      1  C   ACE A   1      33.910  24.800  13.510  1.00  0.00           C
ATOM      2  O   ACE A   1      33.760  24.560  14.700  1.00  0.00           O
ATOM      3  CH3 ACE A   1      33.160  24.100  12.400  1.00  0.00           C
ATOM      4 HH31 ACE A   1      32.860  24.830  11.650  1.00  0.00           H
ATOM      5 HH32 ACE A   1      33.800  23.390  11.880  1.00  0.00           H
ATOM      6 HH33 ACE A   1      32.250  23.650  12.770  1.00  0.00           H
```

Loaded and exported with retain_order set to 1

```
ATOM      1  CH3 ACE A   1      33.160  24.100  12.400  1.00  0.00           C
ATOM      2 HH31 ACE A   1      32.860  24.830  11.650  1.00  0.00           H
ATOM      3 HH32 ACE A   1      33.800  23.390  11.880  1.00  0.00           H
ATOM      4 HH33 ACE A   1      32.250  23.650  12.770  1.00  0.00           H
ATOM      5  C   ACE A   1      33.910  24.800  13.510  1.00  0.00           C
ATOM      6  O   ACE A   1      33.760  24.560  14.700  1.00  0.00           O
```
