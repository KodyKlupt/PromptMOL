# Morph

The morph command is an incentive PyMOL feature (not available in open-source version). Given two or more conformations, either as two objects or one multi-state object, **morph** can create an interpolated trajectory from the first to the second conformation.

- This command is new in PyMOL 1.6, for older versions see rigimol.morph, which requires some scripting.*

##  Usage
 morph name, sele1 [, sele2 [, state1 [, state2 [, refinement [, steps [, method [, match ]]]]]]]

##  Arguments
- name = string: name of object to create
- sele1 = string: atom selection of first conformation
- sele2 = string: atom selection of second conformation {default: }
- state1 = int: sele1 state {default: 1}. If state1=0 and sele1 has N states, create N morphings between all consecutive states and back from state N to 1 (so the morph will have N*steps states). If state2=0, create N-1 morphings and stop at last state.
- state2 = int: sele2 state {default: 2 if sele1=sele2, else 1}
- refinement = int: number of sculpting refinement cycles to clean distorted intermediates {default: 3}
- steps = int: number of states for sele2 object {default: 30}
- method = string: rigimol or linear {default: rigimol}
- match = string: method how to match **sele1** and **sele2** {default: align}
- * in: match atoms by "in" selection operator
- * like: match atoms by "like" selection operator
- * align: match atoms with align function (with cycles=0)
- * super: match atoms with super function (with cycles=0)
- * *name of alignment object*: use given alignment

##  Example
###  Default Parameters
```python
fetch 1akeA 4akeA, async=0
align 1akeA, 4akeA
morph mout, 1akeA, 4akeA
```

###  Morphing with Ligand
Since the default **match=align** method ignores ligands in most situations, we'll use the "in" match method. In this case, both input structures need matching identifiers. The default post-RigiMOL sculpting refinement tends to let all molecules that are not connected to the protein backbone bounce around; that's why **refinement=0** might give better results in this case.

```python
1. get two hemoglobin beta chains, the "ligand" will be the heme hetero group
fetch 1hbb, async=0
create conf1, chain B
create conf2, chain D
delete 1hbb

1. important: identifiers must be the same
alter conf2, chain="B"
alter all, segi=""

1. optional: styling
as cartoon
show sticks, not polymer
show nb_spheres

1. superpose and morph
align conf1, conf2
morph mout, conf1, conf2, match=in, refinement=0
```

##  Refinement
The default procedure performs two steps: (1) RigiMOL, and (2) refinement of non-backbone atoms by sculpting. The second part can be skipped with "refinement=0". The refinement maintains the local sidechain geometry -- based on start and end conformation as references -- and avoids clashes by VDW repulsion.

###  Exclude atoms from refinement
Consider the previous "Morphing with Ligand" example, where refinement was skipped to avoid that the ligand gets pushed out of place. By "fixing" a set of hand-picked atoms we can still perform reasonable refinement:

```python
1. morph without refinement (see "Morphing with Ligand" example)
morph mout, conf1, conf2, match=in, refinement=0

1. exclude the HEM core from moving
flag fix, /mout///HEM/NA+NB+NC+ND+FE extend 1, set

1. do the refinement
import epymol.rigimol
epymol.rigimol.refine(5, "mout")
```

###  Select the sculpting terms
By default, all sculpting terms are used. Just like the sculpt_field_mask setting, the **refine** function takes a **sculpt_field_mask** argument which is a bitmask to select which sculpting terms should be used. For available terms, see:
https://github.com/schrodinger/pymol-open-source/blob/master/layer2/Sculpt.h

Example which uses only bond length and angle terms:

```python
cSculptBond = 0x001
cSculptAngl = 0x002
bondOrAngle = cSculptBond | cSculptAngl

1. do the refinement
import epymol.rigimol
epymol.rigimol.refine(5, "mout", sculpt_field_mask=bondOrAngle)
```

##  GUI
The morph feature is available from the object menu panel: **A > generate > morph**
