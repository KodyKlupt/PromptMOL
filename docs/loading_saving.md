# Loading and Saving Structures

## Fetch from RCSB PDB

```python
cmd.fetch('1ABC')          # downloads 1ABC.cif or .pdb from RCSB
cmd.fetch('1ABC', '1abc')  # fetch and name the object '1abc'
cmd.fetch('1ABC', async_=0)  # synchronous fetch (waits before next line)
```

PDB IDs are always 4 characters. Fetched objects are named by the PDB ID in lowercase.

## Load from local file

```python
cmd.load('path/to/file.pdb', 'myprotein')   # load with object name
cmd.load('file.cif')                         # name auto-derived from filename
cmd.load('file.mol2', 'ligand')
cmd.load('file.sdf', 'compound')
cmd.load('trajectory.dcd', 'protein')        # trajectory
```

Supported formats: pdb, cif, mol2, sdf, mol, xyz, mae, dcd, xtc, trr.

## Save structures

```python
cmd.save(os.path.join(output_dir, 'out.pdb'), 'selection')
cmd.save(os.path.join(output_dir, 'out.pdb'), 'all')
cmd.save(os.path.join(output_dir, 'out.mol2'), 'organic')
cmd.save(os.path.join(output_dir, 'out.sdf'), 'resn LIG')
```

Always use `output_dir` for paths. The second argument is the selection to save.

## Delete objects

```python
cmd.delete('object_name')   # remove a single object
cmd.delete('all')           # clear everything
```

## Get loaded objects

```python
names = cmd.get_object_list()   # list of all loaded object names
names = cmd.get_object_list('polymer.protein')  # filtered
```

## Reinitialize

```python
cmd.reinitialize()   # clear all objects and reset settings (use with caution)
```
