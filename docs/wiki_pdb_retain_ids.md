# Pdb retain ids

##  Overview
If set, atoms and residues are not renumbered when exporting imported pdb. (Must be set before import)

##  Syntax
```python
set pdb_retain_ids,[0,1]
set pdb_retain_ids #default 1
```

##  Example
Loaded and exported with pdb_retain_ids set to 0

```
ATOM     21  CH2 TRP A   2      38.350  22.030  11.200  1.00  0.00           C
ATOM     22  HH2 TRP A   2      38.620  21.010  10.930  1.00  0.00           H
ATOM     23  C   TRP A   2      35.010  27.370  14.910  1.00  0.00           C
ATOM     24  O   TRP A   2      35.380  27.560  16.060  1.00  0.00           O
ATOM     25  CH3 ACE A   1      33.160  24.100  12.400  1.00  0.00           C
ATOM     26 HH31 ACE A   1      32.860  24.830  11.650  1.00  0.00           H
ATOM     27 HH32 ACE A   1      33.800  23.390  11.880  1.00  0.00           H
ATOM     28 HH33 ACE A   1      32.250  23.650  12.770  1.00  0.00           H
ATOM     29  C   ACE A   1      33.910  24.800  13.510  1.00  0.00           C
ATOM     30  O   ACE A   1      33.760  24.560  14.700  1.00  0.00           O
TER      31      ACE A   1
ATOM     32  N   TRP A   3      33.910  27.930  14.400  1.00  0.00           N
ATOM     33  H   TRP A   3      33.670  27.680  13.450  1.00  0.00           H
ATOM     34  CA  TRP A   3      33.080  28.950  15.030  1.00  0.00           C
```

Loaded and exported with pdb_retain_ids set to 1

```
ATOM     27  CH2 TRP A   2      38.350  22.030  11.200  1.00  0.00           C
ATOM     28  HH2 TRP A   2      38.620  21.010  10.930  1.00  0.00           H
ATOM     29  C   TRP A   2      35.010  27.370  14.910  1.00  0.00           C
ATOM     30  O   TRP A   2      35.380  27.560  16.060  1.00  0.00           O
ATOM      1  CH3 ACE A   1      33.160  24.100  12.400  1.00  0.00           C
ATOM      2 HH31 ACE A   1      32.860  24.830  11.650  1.00  0.00           H
ATOM      3 HH32 ACE A   1      33.800  23.390  11.880  1.00  0.00           H
ATOM      4 HH33 ACE A   1      32.250  23.650  12.770  1.00  0.00           H
ATOM      5  C   ACE A   1      33.910  24.800  13.510  1.00  0.00           C
ATOM      6  O   ACE A   1      33.760  24.560  14.700  1.00  0.00           O
TER       7      ACE A   1
ATOM     31  N   TRP A   3      33.910  27.930  14.400  1.00  0.00           N
ATOM     32  H   TRP A   3      33.670  27.680  13.450  1.00  0.00           H
ATOM     33  CA  TRP A   3      33.080  28.950  15.030  1.00  0.00           C
```
