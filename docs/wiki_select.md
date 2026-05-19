# Select

- *select** creates a named selection from an atom selection.  Selections are one of the most powerful aspects of PyMOL and learning to use selections well is paramount to quickly achieving your goals in PyMOL.

##  Usage
 select name [, selection [, enable [, quiet [, merge [, state ]]]]]

Convenience shortcut to create selection with name "sele":

 select (selection)

##  Arguments
- **name** = str: a unique name for the selection {default if skipped: sele}
- **selection** = str: a selection-expression
- **enable** = 0/1: show selection indicators {default: 1}
- **quiet** = 0/1 {default: 0 for command, 1 for API}
- **merge** = 0/1: update existing named selection {default: 0}
- **state** = int: object state, affects spacial operators like **within** {default: 0 (all states)}

##  Examples
 select near , (ll expand 8)
 select near , (ll expand 8)
 select bb, (name CA+N+C+O)

```python
cmd.select("%s_%s"%(prefix,stretch), "none")
```
