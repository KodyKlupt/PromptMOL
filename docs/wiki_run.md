# Run

- *run** executes an external Python script in a local name space, the global namespace, or in its own namespace (as a module).

### USAGE
 run python-script [, (local | global | module | main | private ) ]

### PYMOL API
Not directly available.  Instead, use :
 cmd.do("run ...").

### NOTES
The default mode for run is **global**.

Due to an idiosyncrasy in Pickle, you can not pickle objects directly created at the main level in a script run as "module", (because the pickled object becomes dependent on that module). Workaround: delegate construction to an imported module.
