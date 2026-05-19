# Auto show classified

When loading structure files, the auto_show_classified setting sets up representations based on molecule classification (depends on auto_classify_atoms).

Available from the Tcl/Tk menu: **Setting > Auto Show ... > ...**

- New in PyMOL 1.8.2*

##  Example
 set auto_show_classified
 fetch 1rx1

##  Values
- -1: for less than 500k atoms: like 1, else like 3 (default, new in PyMOL 2.0)
- 0: off (default in PyMOL 1.8)
- 1: show polymer as cartoon, organic as sticks, and inorganic as spheres
- 2: like 1, but apply auto_show_lines and auto_show_nonbonded in addition
- 3: simplified version, show polymer as ribbon, organic and inorganic as lines or nonbonded
