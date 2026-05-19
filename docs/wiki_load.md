# Load

- *load** reads several file formats.  The file extension is used to determine the format.  PDB files must end in ".pdb", MOL files must end in ".mol", Macromodel files must end in ".mmod", XPLOR maps must end in ".xplor", CCP4 maps must end in ".ccp4", Raster3D input (Molscript output) must end in  ".r3d", PyMOL session files must end in ".pse", and pickled ChemPy models with a ".pkl" can also be directly read.

If an object is specified, then the file is loaded into that object. Otherwise, an object is created with the same name as the file prefix.

### USAGE
```python
load filename [,object [,state [,format [,finish [,discrete [,multiplex ]]]]]]
```

### PYMOL API
```python
cmd.load( filename [,object [,state [,format [,finish [,discrete [,multiplex ]]]]]] )
```

### ARGUMENTS
- **filename : string** Path or URL to the file to load.
- **object : string** Name of Pymol object to store the structure in. Defaults to the filename prefix.
- **state : integer** State number to store the object in, or 0 to append (default:0)
- **format : string** Format for the file (see notes). Defaults to the filename extension.
- **finish : integer**
- **discrete : integer** For multi-model structures, a value of 0 indicates that models have the same set of atoms (e.g. trajectory files or NMR structures), allowing memory savings, while a value of 1 forces the creation of independent atom sets for each model {default: -1 (file type dependent)} (see discrete objects)
- **quiet : integer** (default 1)
- **multiplex : integer** Load a multi-model file as separate objects instead of states (see also split_states)
- **zoom : integer** {default: -1 = use auto_zoom setting}
- **partial : integer** For session files (.pse). partial=0: discard current session. partial=1: merge with current session (will not load global settings, selections, movie, camera). partial=2: like 1, but also load camera view {default: 0}
- **mimic : integer** For .mae files, match style from file as close as possible, uses atom-level settings (like cartoon_color) {default: 1}
- **object_props : string** = Space delimited list of property names (or * wildcard) to load from .sdf or .mae files {default: use load_object_props_default setting} *Incentive PyMOL 1.6+*
- **atom_props : string** = Space delimited list of property names (or * wildcard) to load from .mae files {default: use load_atom_props_default setting} *Incentive PyMOL 1.6+*

### NOTES
- You can override the file extension by giving a format string:

 'pdb' : PDB,  'mmod' : Macromodel, 'xyz' : Tinker, 'cc1' : ChemDraw3D
 'mol' : MDL MOL-file, 'sdf' : MDL SD-file
 'xplor' : X-PLOR/CNS map, 'ccp4' : CCP4 map,
 'callback' : PyMOL Callback object (PyOpenGL)
 'cgo' : compressed graphics object (list of floats)
 'trj' : AMBER trajectory (use load_traj command for more control)
 'top' : AMBER topology file 'rst' : AMBER restart file
 'cex' : Metaphorics CEX format
 'pse' : PyMOL Session file
 'pqr' : PQR (a modified PDB file with charges and radii)
 'mol2' : MOL2

- A new feature has been added to load.  You can specify an URL to a PDB and PyMOL will download it.  This is a very handy feature for loading experimental/theoretical data from servers across the web.  Just copy the link they give you and do,

```python
load http://www.theurl.com/path/toYourData
```

or you can open a remote file just from the command line

```
1. load a PDB file; I placed one example file on the PyMOL Wiki
pymol http://www.pymolwiki.org/1rsy.pdb

1. PyMOL can also handle the gzipped files on the PDB.  :-)
pymol ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/00/pdb100d.ent.gz
```

### User Comments/Examples
- Load xyz.pdb using the PyMOL API:

```python
cmd.load("xyz.pdb")
```

- Loading multiple PDBs into one object with many states:

```python
load trj0001.pdb, mov
load trj0002.pdb, mov
load trj0003.pdb, mov
etc.
```

or, if you have too many states to do that by hand,

```python
for idx in range(1,1001):cmd.load("trj%04d.pdb"%idx,"mov")
```

or, you can use "glob" from Python,

```python
from glob import glob
lst = glob("trj*.pdb")
lst.sort()
for fil in lst: cmd.load(fil,"mov")
```

- Load a NAMD multi-PDB file.  These are just concatenated PDB files.

```python
load NAMDtrajFile.pdb, multiplex=0
```

- Hint: You can save some time & a lot of memory by loading the file and removing the atoms in a single-line compound statement (with a semicolon
after the load statement).

```python
load 1E3M.pdb; remove not A-C+F//
```

- Decorating the load command to include technical info about the loaded object

```python
def load_with_props(fileName, objName):
  # store whatever info you want, like the filename
  obj_info[objName] = fileName
  # ... do more recording of properties you choose
  # ask PyMOL to now load the file
  cmd.load(fileName,objName)
```

Then on can query obj_info based on the object name:

```python
for obj in cmd.get_names():
  print obj_info[obj]
```

### SEE ALSO
Fetch Save Load Traj
