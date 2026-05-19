# Cache

Cache manages storage of precomputed results, such as molecular surfaces.

= Usage =

```python
cache action [, scenes [, state ]]
```

where, the arguments are:

- *action**
:: string: enable, disable, read_only, clear, or optimize
- *scenes**
::string: a space-separated list of scene names (default: '')
- *state**
::integer: state index (default: -1)

= Examples =

```python
cache enable
cache optimize
cache optimize, F1 F2 F5
```


= Notes =
"cache optimize" will iterate through the list of scenes provided (or all defined scenes), compute any missing surfaces, and store them in the cache for later reuse.

= API =

```python
cmd.cache(string action, string scenes, int state, int quiet)
```
