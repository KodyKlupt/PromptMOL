# CBC

Util.cbc stands for (the utilities library's) **color by chain**.  This simply colors molecules by their chains, as the name suggests.

The affects of CBC are shown in the following images.

Image:Cbc0.png|Molecule loaded
Image:Cbc1.png|util.cbc command issued.  Each chain gets its own color.

##  Usage
```python
1. simple command
util.cbc selection, first_color, quiet

1. api usage
util.cbc(selection='(all)',first_color=7,quiet=1,legacy=0,_self=cmd)
```

where
- selection defaults to 'all',
- first_color defaults to 7,
- quiet defaults to 1

##  Example
```python
1. color everything by chain
util.cbc
```
