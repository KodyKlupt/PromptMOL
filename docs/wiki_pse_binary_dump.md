# Pse binary dump

The pse_binary_dump setting affects the PyMOL session file format (.pse). If set to **on**, session export will be significantly faster and produce smaller files.

- New in PyMOL 1.8*

##  Examples
```python
fetch 1ubq

set pse_binary_dump, off
save regular.pse

set pse_binary_dump, on
save binary.pse

1. compare file size
print(os.path.getsize("regular.pse"))   # prints 215482
print(os.path.getsize("binary.pse"))    # prints 118557
```

##  Known Limitations
- Before 2.4: Atom Properties not supported
