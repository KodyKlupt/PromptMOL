# Super

- *super** aligns two selections.
It does a **sequence-independent** (unlike align) structure-based dynamic programming alignment followed by a series of refinement cycles intended to improve the fit by eliminating pairing with high relative variability (just like align).
- *super** is more robust than **align** for proteins with low sequence similarity.

##  Usage
See align command.

##  Caveats
- **Alternative Conformations:**  If super ever tells you no matched atoms, then instead of
```python
super p1, p2
```
 try
```python
super p1 & alt A+*, p2 & alt B+*
```

##  User Scripts
###  Write rmsd to file
- *pymol_rmsd_test.pml**

```python
reinitialize

fetch 1F9J, async=0
fetch 1YX5, async=0

extract 1F9J_A, 1F9J and chain A
extract 1YX5_B, 1YX5 and chain B

test=cmd.super("1F9J_A","1YX5_B")

python
writefile=open("rmsd_file.txt","a")
writefile.write(' '.join('%s' % x for x in test))
writefile.write('\n')
writefile.close()
python end
```

In terminal

```
pymol -c pymol_rmsd_test.pml ; tail -n 1 rmsd_file.txt
```

###  Write rmsd to file and looping
- *pymol_pymol_loop.sh**

```
1. !/bin/csh -f
set x = 1

while ( $x <= 20 )
	set prot="energy_${x}.pdb"
	pymol -c pymol_super.pml $prot
	@ x = $x + 1
end
```

- *pymol_super.pml**

```python
reinitialize
import sys

python
prot1="XXXX"
prot2="YYYY_trimmed"

prot3=sys.argv[3]
1. prot3="energy_54.pdb"
prot3name=prot3.split(".pdb")[0]
print prot3, prot3name
python end

cd /XXXXX

cmd.load("%s.pdb"%prot1)
cmd.load("%s.pdb"%prot2)
cmd.load("./ensemblesize2_numstruct/%s"%prot3)
1. show_as cartoon, all

align1=cmd.super("%s"%prot3name,"%s"%prot1)
print align1

python
writefile=open("pymol_rmsd_file.txt","a")
writefile.write('%s %s '%(prot3name, prot1))
writefile.write(' '.join('%s' % x for x in align1))
writefile.write(' ')
python end

align2=cmd.super("%s"%prot3name,"%s"%prot2)
print align2

python
writefile=open("pymol_rmsd_file.txt","a")
writefile.write('%s %s '%(prot3name, prot2))
writefile.write(' '.join('%s' % x for x in align2))
writefile.write('\n')
writefile.close()
python end
```

In terminal

```
chmod +x pymol_loop.sh
./pymol_loop.sh
```
