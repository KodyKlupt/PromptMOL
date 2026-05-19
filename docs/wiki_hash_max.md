# Hash max

##  Overview
hash_max sets how much memory PyMOL uses when ray tracing.
Higher values will enable PyMOL to ray trace more quickly, provided you can secure the necessary memory. Thus for large scenes,  it can be useful to increase this value.  Simpler scenes probably don't need it.  If **hash_max** is set too high, then PyMOL can (and will) crash when it attempts to use more memory than available.
Likewise, **hash_max** can be used to limit the use of memory to avoid crashes at the expense of increased computing time.

##  Syntax
```python
set hash_max, int
```

where **int** is a positive integer.  The default value is 100.

##  Example
```python
set hash_max, 200
```
