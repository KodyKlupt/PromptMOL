# Rms cur

rms_cur computes the RMS difference between two atom selections without performing any fitting.

By default, only matching atoms in both selections will be used for the fit (same chain, residue number, atoms names etc.). Alternate location mess up the match!

##  Usage
 rms_cur mobile, target [, mobile_state [, target_state [, quiet [, matchmaker [, cutoff [, cycles [, object ]]]]]]]

##  Arguments
See fit.

##  Examples
###  Example 1: Identical Identifiers
Alternate location mess up the match, so remove them first.

 fetch 1p36 1kw7, async=0
 remove not alt ""+"A"
 rms_cur 1p36, 1kw7

###  Example 2: Homologues
Use align or super to create an alignment object (without fitting) and then use the alignment object in the atom selection and turn off identifier matching with **matchmaker=-1**.

 fetch 1oky 1t46, async=0

 # create alignment object
 align 1oky, 1t46, cycles=0, transform=0, object=aln

 # RMSD of alignment object
 rms_cur 1oky & aln, 1t46 & aln, matchmaker=-1
