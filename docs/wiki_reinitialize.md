# Reinitialize

- *reinitialize** reinitializes PyMOL.  Issuing the command 'reinitialize' during a PyMOL session clears all objects and resets all parameters to defaults; this is equivalent to re-starting the program without having to actually do so.

- NOTE: any unsaved work will be lost!
- NOTE: Multi-CPU machines will sometimes lose SMP abilities in PyMol after running this command.
- NOTE: settings that usually load with a .pymolrc file will also not work

Alternatively, this command can reset all settings to default values.

### USAGE
 reinitialize [what [, object]]

### ARGUMENTS
- what = string: everything|settings {default: everything}

- object = string: object name for per object settings

### SEE ALSO
Delete all
