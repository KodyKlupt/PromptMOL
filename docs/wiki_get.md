# Get

get returns the value of a setting.

This command is very useful for determining the any setting(s) when writing a script.  For example, with this command you can find out if the background is opaque, where the light source is, etc.

=USAGE=

```python
get name [, selection [, state ]]
```

=Examples=

```python
get opaque_background

get line_width
```

=PYMOL API=

```python
print cmd.get(string name, string object, int state, int quiet)
```


=Notes=
- The API command will not print out and should be stored or used for comparison
- "get" currently only works with global, per-object, and per-state settings.  There is currently no way to retrieve per-atom settings.

=SEE ALSO=
Set
