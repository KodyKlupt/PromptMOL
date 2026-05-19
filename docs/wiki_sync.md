# Sync

sync is an API-only function which waits until all current commands have been executed before returning.  A timeout can be used to insure that this command eventually returns.

## PYMOL API
```python
cmd.sync(timeout: float = 1.0, poll: float = 0.05)
```
