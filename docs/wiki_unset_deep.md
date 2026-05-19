# Unset deep

The unset_deep command clears settings on the object, object-state, atom and bond levels.

- New in PyMOL 1.8.4*

##  Usage
 unset_deep [ settings [, object ]]

##  Arguments
- **settings** = str: space separated list of setting names or empty string for all settings {default: }
- **object** = str: name of one object or * for all objects {default: *}

##  Example
 fetch 1rx1, async=0
 as cartoon
 color green

 # object-level
 set cartoon_color, blue, 1rx1

 # atom-level
 set cartoon_color, red, resi 20-30

 # clear on all levels
 unset_deep cartoon_color

##  Note
Does currently not unset atom-state level settings.
