# Attach

- *attach** adds a single atom onto the picked atom.

## USAGE
 attach element, geometry, valence

## PYMOL API
 cmd.attach( element, geometry, valence )

##  ARGUMENTS
- element = string: element name (symbol) of the added atom. Case-sensitive.

- geometry = int: geometry (steric number) of added atom.

- valence = int: valence of the added atom.

##  EXAMPLE
```python
attach O, 1, 1 # adds an Oxygen atom to picked atom.
```
