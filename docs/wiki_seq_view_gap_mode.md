# Seq view gap mode

The seq_view_gap_mode setting controls if gap indicators are displayed in the sequence viewer.

- New in PyMOL 2.3*

##  Values
- 0: no gap indicator display
- 1: number of dashes equals number of missing residues (based on residue numbers) {default}
- 2: one dash per gap (independent of size)

##  Example
 fetch 2xwu, type=pdb, async=0
 set seq_view_gap_mode, 1
 set seq_view

Scroll sequence viewer to chain B residue 152, it should display 3 dashes.
