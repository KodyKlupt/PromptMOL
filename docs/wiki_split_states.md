# Split states

- *Split_States** splits and orients multiple models and multimers from the biological unit file into a set of single-state molecular objects.

##  Syntax
```python
split_states object [, first [, last [, prefix ]]]
```

This splits the **object** from **first** to **last** out to the array of objects prefixed by **prefix**.  The **prefix** option is very handy if all your states--or a subset of the states--have the same name.

## Using
To use **split_states** simply
Load your molecule

```python
1. example usage
load fileName.pdb1, name
split_states name
delete name

1. split all the states to objects starting with conf
fetch 1nmr
split_states 1nmr, prefix=conf
```

## Example
- *1VLS**: A dimer.

```python
load 1vls.pdb1, 1vls
split_states 1vls
dele 1vls
```

Image:1vls1.png|1VLS as a monomer.  This is the state of 1VLS when I load the molecule (and select cartoon representation).
Image:1vls1_dimer.png|1VLS as a dimer using the split_states command.  Notice PyMOL automatically loads and orients the new molecules.

= See Also =
- PDB Tutorial Biological Units
