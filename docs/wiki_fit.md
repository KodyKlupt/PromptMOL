# Fit

Fit superimposes the model in the first selection on to the model in the second selection.  Only *matching atoms* in both selections will be used for the fit.

### USAGE
 fit mobile, target [, mobile_state [, target_state [, quiet [, matchmaker [, cutoff [, cycles [, object ]]]]]]]

###  ARGUMENTS
- **mobile** = string: atom selection
- **target** = string: atom selection
- **mobile_state** = integer: object state {default=0, all states)
- **target_state** = integer: object state {default=0, all states)
- **matchmaker** = integer: how to match atom pairs {default: 0}
- * -1: assume that atoms are stored in the identical order
- * 0/1: match based on all atom identifiers (segi,chain,resn,resi,name,alt)
- * 2: match based on ID
- * 3: match based on rank
- * 4: match based on index (same as -1 ?)
- **cutoff** = float: outlier rejection cutoff (only if cycles>0) {default: 2.0}
- **cycles** = integer: number of cycles in outlier rejection refinement {default: 0}
- **object** = string: name of alignment object to create {default: None}

### EXAMPLES
```python
fit ( mutant and name ca ), ( wildtype and name ca )
```

If atom identifiers (like segi, chain, ...) in mobile and target do not match, you need to alter them (or use Pair_Fit instead):

```python
fetch 1a00, async=0
extract hbaA, chain A
extract hbaC, chain C
1. hbaA and hbaC are the same protein, but have different chain identifiers
alter hbaC, chain='A'
alter hbaC, segi='A'
1. now both have identical atom identifiers
fit hbaC, hbaA
```

### SEE ALSO
Rms, Rms_Cur, Intra_Fit, Intra_Rms, Intra_Rms_Cur, Pair_Fit
