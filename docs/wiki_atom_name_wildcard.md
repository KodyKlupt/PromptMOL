# Atom name wildcard

## OVERVIEW
This setting controls whether or not PyMOL will respect wildcards ("*").  PyMOL automatically disables the asterisk wildcard for atom names in PDB structures read which contain asterisks in the atom name field (as many NA structures do).

## USAGE
The following code will restore wildcard usage in PyMOL, if it has been turned off.

```python
1. allow wildcards
unset atom_name_wildcard, object-name
```

- *Please note**, however, that PyMOL will then be unable to distinguish **C2** in the base from **C2*** in the sugar.

If, before running the previous command, you instead issue the following command:

```python
1. change all '*'s in names to "'"
alter all, name=name.replace("*","'")
```

you will be able to distinguish C2 from C2' and still have your atom
name wildcards!
