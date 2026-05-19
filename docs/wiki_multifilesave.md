# Multifilesave

The multifilesave command saves each object and/or state in a selection
to a separate file.

- New in PyMOL 2.1*

##  Usage
 multifilesave filename [, selection [, state [, format ]]]

The **filename** argument must contain one or more placeholders:

 {name}  : object name
 {state} : state number
 {title} : state title
 {num}   : file number
 {}      : object name (first) or state (second)

##  Arguments
- **filename** = str: file path with placeholders
- **selection** = str: atom selection {default: all}
- **state** = int: object state (-1 for current, 0 for all states) {default: -1}
- **format** = str: file format, e.g. pdb {default: guess from file extension}

##  Examples
 multifilesave /tmp/{name}.pdb
 multifilesave /tmp/{name}-{state}.cif, state=0
 multifilesave /tmp/{}-{}.cif, state=0
 multifilesave /tmp/{}-{title}.sdf, state=0
