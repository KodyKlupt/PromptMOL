# Fetch Path

Fetch_Path sets the default path that PyMOL uses to load files from *before* it tries to download them from the PDB.

= Details =
If you have a local copy of the PDB on your machine, say in directory **/spc/pdb** then, once you set Fetch_Path to that directory the fetch command will look in **/spc/pdb** before going to the PDB for your file.  Also, the files fetched from the PDB are stored here once downloaded. PyMOL will only look for files starting with the pdb code in lower case.

= Examples =

On Linux or MacOS:

```python
set fetch_path, /spc/pdb
```

On Windows:

```python
set fetch_path, D:\mypdbs
```

Using ~/fetch_path:

```python
cmd.set('fetch_path', cmd.exp_path('~/fetch_path'), quiet=0)
```

= Hints =

Put this in your pymolrc to make it permanent.

= See Also =
- fetch
- pymolrc
