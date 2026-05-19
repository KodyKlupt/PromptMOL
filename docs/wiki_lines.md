# Lines

- *Lines** is name of the basic representation for atoms and bonds in PyMOL.  **Lines** is a very simple representation, where each atom bond is displayed as a single colored line, and each atom is displayed as the intersection of any two or more non-terminal bonds.

=Usage=

```python
1. show everything as lines
show lines

1. only show residues 50-80 as lines
show lines, i.50-80
```

## Examples
### Example: Displaying dashed lines between two atoms
The following commands will create a dashed line between two atoms.

```python
1. first, create two named selections
select a, ///A/501/02
select b, ///B/229/N
1. calculate & show the distance from selection a to selection b.
distance d, a, b
1. hide just the distance labels; the
1. dashed bars should still be shown
hide labels, d
```

Technically, the object *d* is a labelled distance, only the label is hidden.
When ray-tracing the image, the dashes come out a bit fat. You can slim them with

```python
set dash_gap, 0.5
set dash_radius, 0.1
```

before the 'ray' command.
