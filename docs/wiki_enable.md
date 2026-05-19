# Enable

The **enable** command toggles on the display of all currently visible representations of an object.  It is the equivalent of selecting the object in the list at the top of the Internal GUI.
### USAGE
 enable [name [, parents]]

; name
: the name of an object or a named selection (default="all")

; parents
: when set to 1, enables the named object and all parent objects of the named object (recursively), so it won't be hidden by having a parent object (or group) that is disabled (default=0)

### PYMOL API
```python
cmd.enable( string name='all', int parents=0 )
```


### EXAMPLES
 enable my_object
 enable (my_object1 or my_object2)
 enable my_object*
 enable
 enable my_object, parents=1

### SEE ALSO
Show, Hide, Disable, Suspend_updates
