# Undo

- (Incentive PyMOL only feature)*

Most actions as of **Incentive PyMOL 2.5** are undoable.

Actions are undoable via GUI menu (Edit -> Undo). The undo feature may be manually disabled by unchecking `Edit -> Undo Enabled`, and can be re-enabled by rechecking the same menu item.

##  Usage
 undo [, steps]

- **steps** = integer: number of steps to undo

##  PyMOL API
```python
cmd.undo(int steps=1)
```

undo_enable is an API-only feature that allows you enable undo.

```python
cmd.undo_enable()
```

undo_disable is an API-only feature that allows you disable undo.

```python
cmd.undo_disable()
```

##  Example
  undo
  undo 5

##  Comments
Currently, the undo stack supports the previous 25 actions or up to 1GB memory used. These will later be configurable in an upcoming release.

Currently, undo support for builder is not available but will be supported in a later patch release.

While movie is playing, the undo manager is paused and will save the current session's state when the user ends the movie.

During wizards, the undo manager is paused, and the current session's state is saved when the user clicks 'Done' for active wizards.

For larger sessions, it may be suitable to manually turn off undo to save on memory usage (commands such as set will incur a high memory cost). Add cmd.undo_disable() in your pymolrc if you need to disable undo automatically upon startup.

For **Incentive PyMOL**, all previous undo features are deprecated and will now be superseded by the one introduced in **Incentive PyMOL 2.5**.
