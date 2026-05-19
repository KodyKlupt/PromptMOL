# Multisave

The multisave command can save a multi-entry PDB file.

Every object in the given selection will have a HEADER record, and is terminated with END. Loading such a multi-entry PDB file into PyMOL will load each entry as a separate object.

This behavior is different to the save command, where a multi-object selection is written "flat" to a PDB file, without HEADER records.

- Older versions could also export a proprietary binary "pmo" file format with this command. However, "pmo" format never supported multiple entries, support was partially broken in in the 1.7 and 1.8 versions, and was finally removed in 1.8.4.*

##  Changes in PyMOL 1.8.4
- CRYST1 records are written if symmetry is defined
- Interpret "pattern" argument as an atom selection. Previous versions expected an object name pattern or a list of objects.
- dropped "pmo" format support

##  Usage
 multisave filename [, pattern [, state [, append ]]]

##  Arguments
- **filename** = str: file path to be written
- **pattern** = str: atom selection (before 1.8.4: object name pattern)
- **state** = int: object state (-1=current, 0=all) {default: -1}
- **append** = 0/1: append to existing file {default: 0}

##  Example
```python
fragment ala
fragment gly

1. PyMOL >= 1.8.4 will write CRYST1 records
set_symmetry ala, 50.840, 42.770,  28.950, 90, 90, 90, P 21 21 21
set_symmetry gly, 99.930, 99.930, 276.840, 90, 90, 90, P 31 2 1

multisave multi.pdb
```

Exported file "multi.pdb":

 HEADER    ala
 CRYST1   50.840   42.770   28.950  90.00  90.00  90.00 P 21 21 21    0
 ATOM      1  N   ALA     2      -0.677  -1.230  -0.491  1.00  0.00           N
 ATOM      2  CA  ALA     2      -0.001   0.064  -0.491  1.00  0.00           C
 ATOM      3  C   ALA     2       1.499  -0.110  -0.491  1.00  0.00           C
 ATOM      4  O   ALA     2       2.030  -1.227  -0.502  1.00  0.00           O
 ATOM      5  CB  ALA     2      -0.509   0.856   0.727  1.00  0.00           C
 ATOM      6  H   ALA     2      -0.131  -2.162  -0.491  1.00  0.00           H
 ATOM      7  HA  ALA     2      -0.269   0.603  -1.418  1.00  0.00           H
 ATOM      8 1HB  ALA     2      -1.605   1.006   0.691  1.00  0.00           H
 ATOM      9 2HB  ALA     2      -0.285   0.342   1.681  1.00  0.00           H
 ATOM     10 3HB  ALA     2      -0.053   1.861   0.784  1.00  0.00           H
 END
 HEADER    gly
 CRYST1   99.930   99.930  276.840  90.00  90.00  90.00 P 31 2 1      0
 ATOM      1  N   GLY    22      -1.195   0.201  -0.206  1.00  0.00           N
 ATOM      2  CA  GLY    22       0.230   0.318  -0.502  1.00  0.00           C
 ATOM      3  C   GLY    22       1.059  -0.390   0.542  1.00  0.00           C
 ATOM      4  O   GLY    22       0.545  -0.975   1.499  1.00  0.00           O
 ATOM      5  H   GLY    22      -1.558  -0.333   0.660  1.00  0.00           H
 ATOM      6 3HA  GLY    22       0.482   1.337  -0.514  0.00  0.00           H
 ATOM      7  HA  GLY    22       0.434  -0.159  -1.479  1.00  0.00           H
 END
