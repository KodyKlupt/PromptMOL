# Rigimol.morph

The morph command is an incentive PyMOL feature (not available in open-source version). Given a two-state object, **morph** can create an interpolated trajectory from the first to the second conformation.

- Notice: There is a new morph command in PyMOL 1.6*

##  Usage
 morph source, target [, first [, last [, refinement [, async [, steps ]]]]]

##  Arguments
- source = string: name of two-state input object
- target = string: name of output object to create
- first = int: start state of source {default: 1}
- last = int: end state of source {default: 2}
- refinement = int: number of sculpting refinement cycles to clean distorted intermediates {default: 10}
- steps = int: number of states for target object {default: 30}

- Warning: arguments first, last and steps new in PyMOL 1.5 (up to 1.4 they are always at default values)*

##  Example
```python
1. get open and closed conformation of adenylate kinase
fetch 1ake 4ake, async=0

1. make two state object
align 1ake and chain A, 4ake and chain A, cycles=0, object=aln
create rin, 1ake and aln, 1, 1
create rin, 4ake and aln, 1, 2

1. morph
from epymol import rigimol
rigimol.morph("rin", "rout")
```

##  PyMOL Command
if you prefer PyMOL syntax over python syntax, add this to your pymolrc file:

```python
import epymol.rigimol
cmd.extend('morph', epymol.rigimol.morph)
```
