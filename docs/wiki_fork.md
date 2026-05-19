# Fork

- *spawn** launches a Python script in a new thread which will run concurrently with the PyMOL interpreter. It can be run in its own namespace (like a Python module, default), a local name space, or in the global namespace.

- *fork** is an alias for **spawn**.

### USAGE
 spawn python-script [, ( local | global | module | main | private )]

### PYMOL API
Not directly available.  Instead, use cmd.do("spawn ...").

### NOTES
The default mode for spawn is "module".

Due to an idiosyncracy in Pickle, you can not pickle objects directly created at the main level in a script run as "module", (because the pickled object becomes dependent on that module).  Workaround: delegate construction to an imported module.

The best way to spawn processes at startup is to use the -l option (see "help launching").

###  SEE ALSO
- run
