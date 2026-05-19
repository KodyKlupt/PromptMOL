# Feedback

feedback allows you to change the amount of information output by pymol.

## USAGE
 feedback action,module,mask

- action is one of ['set','enable','disable']
- module is a space-separated list of strings or simply "all"
- mask is a space-separated list of strings or simply "everything"

## PYMOL API
```python
cmd.feedback(string action,string module,string mask)
```

## EXAMPLES
 feedback enable, all , debugging
 feedback disable, selector, warnings actions
 feedback enable, main, blather
