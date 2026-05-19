# Order

### DESCRIPTION
- *order** allows you to change ordering of names in the control panel

### USAGE
 order names-list, sort, location

#### EXAMPLES
```python
1. sets the order of these three objects
order 1dn2 1fgh 1rnd

1. sorts all names
order *,yes

1. sorts all names beginning with 1dn2_
order 1dn2_*, yes

1. puts 1frg at the top of the list
order 1frg, location=top
```

### PYMOL API
```python
cmd.order(string names-list, string sort, string location)
```

### NOTES
1. names-list: a space separated list of names
1. sort: yes or no
1. location: top, current, or bottom

### SEE ALSO
Set_Name
