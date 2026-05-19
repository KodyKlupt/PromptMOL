# Alias

- *alias** allows you to bind a commonly used command to a single PyMOL keyword.

### USAGE
 alias name, command-sequence

### PYMOL API
 cmd.alias(string name,string command)

### EXAMPLES
 alias go,load $TUT/1hpv.pdb; zoom 200/; show sticks, 200/ around 8 go

### NOTES
For security reasons, new PyMOL commands created using "extend" are not saved or restored in sessions.

### SEE ALSO
extend, api
