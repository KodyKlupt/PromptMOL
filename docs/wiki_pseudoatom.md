# Pseudoatom

pseudoatom creates a molecular object with a pseudoatom or adds a pseudoatom to a molecular object if the specified object already exists. Default position is in the middle of the viewing window.

##  USAGE
```python
pseudoatom object [, selection [, name [, resn [, resi [, chain
        [, segi [, elem [, vdw [, hetatm [, b [, q [, color [, label
        [, pos [, state [, mode [, quiet ]]]]]]]]]]]]]]]]]
```

##  ARGUMENTS
- object = string: name of object to create or modify

- selection = string: optional atom selection. If given, calculate position (pos) as center of this selection (like center of mass without atom masses).

- name, resn, resi, chain, segi, elem, vdw, hetatm, b, q = string: atom properties of pseutoatom

- color = string: color of pseudoatom

- label = string: place a text label and hide all other representations

- pos = 3-element tuple of floats: location in space (only if no selection given)

- state = integer: state to modify, 0 for current state, -1 for all states {default: 0}

- mode = string: determines the vdw property if vdw is not given. Either as RMS distance (mode=rms, like radius of gyration without atom masses) or as maximum distance (mode=extent) from pseudoatom to selection {default: rms}

```python
1. create the pseudoatom
pseudoatom tmpPoint
 ObjMol: created tmpPoint/PSDO/P/PSD`1/PS1
1. show it as a sphere.
show spheres, tmpPoint

1. create another, with more options.
pseudoatom tmpPoint2, resi=40, chain=ZZ, b=40, color=tv_blue, pos=[-10, 0, 10]
 ObjMol: created tmpPoint2/PSDO/ZZ/PSD`40/PS1
```

##  EXAMPLES FOR USE
pseudoatom can be used for a wide variety of tasks where on must place an atom or a label in 3D space, e.g. as a placeholder for distance measurement or distance specifications.

```python
1. A pseudoatom as a placeholder for selections according to distance:
load $TUT/1hpv.pdb
pseudoatom tmp, pos=[10.0, 17.0, -3.0]
show sticks, tmp expand 6
delete tmp

1. A pseudoatom as placeholder for distance measurement:
1. position it at the center of an aromatic ring.  Then
1. calc the distance from another atom to the pseudoatom.
load $TUT/1hpv.pdb
pseudoatom pi_cent,b/53/cg+cz
dist pi_cent////ps1, b/met`46/ce
```

You can use a pseudoatom to make a label for a scene title. Move the protein to the bottom of the window before the pseudoatom is created. Or move the label after creating it (Shift + Middle mouse button in editing mode).

```python
fetch 1rq5
pseudoatom forLabel
label forLabel, "This Protein is a Carbohydrate Active Enzyme"
set label_color, black
1. png ray=1
```

Image:Patom.png|You can use a pseudoatom for a movable scene label.
Image:Pseu1.png|Example of using a pseudoatom for distance measurement.
