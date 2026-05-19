# Copy

- *copy** creates a new object that is an identical copy of an existing object

### USAGE
```python
copy target, source
```

### PYMOL API
```python
cmd.copy(string target,string source)
```

### SEE ALSO
- create

### User Comments/Examples
```python
## will copy the object "trna" into six new objects with a number suffic
s = range(6)
for x in s:
	cmd.copy("trna%s" %x, "trna")
```
