# Rms

Rms computes a RMS fit between two atom selections, but does not tranform the models after performing the fit.

### USAGE
```python
rms (selection), (target-selection)
```

### EXAMPLES
```python
fit ( mutant and name ca ), ( wildtype and name ca )
```

### USER COMMENTS
To determine the RMS without any fitting, see Rms_Cur

Fit, Rms, Rms_Cur are finicky and only work when all atom identifiers match: segi, chain, resn, name, alt.  If they don't then you'll need to use the alter command to change the identifiers to that they do -- typically that means clearing out the SEGI field, renaming chains, and sometimes renumbering.

I tried made two selections A, and D as

 PyMOL>sel A, 1gh2 and n. CA and i. 65-99
 Selector: selection "A" defined with 35 atoms.
 PyMOL>sel D, 1kao and n. CA and i. 64-98
 Selector: selection "D" defined with 35 atoms
which as you can see both yield 35 atoms.  Now,

 rms_cur A, D
won't work, due to the aforementioned reason.  To fix this, one needs to do,

 alter all,segi=""
 alter all,chain=""
 alter D, resi=str(int(resi)+1)  # I don't actually use this line
and now

 rms_cur A, D

should work.

### SEE ALSO
Fit, Rms_Cur, Intra_Fit, Intra_Rms, Intra_Rms_Cur, Pair_Fit

Warren DeLano's comment on rms_* and commands.
