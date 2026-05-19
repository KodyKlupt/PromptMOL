# Internal feedback

= Overview =
The Internal_feedback is the openGL-based command line area.  Setting this to 0 removes the area; setting it to 1 makes one line visible (so you can see what you're typing); or you can set it to a higher value and see more lines internally (see images below).

Image:InternalFeedback1.png|Internal_feedback set to 1
Image:InternalFeedback10.png|Internal_feedback set to 10.

= Syntax =

```python
1. set the number of lines shown to 'int', where int is
1. an integer >= 0.
set internal_feedback, int

1. For example, show 10 lines of internal feedback
set internal_feedback, 10
```

= See Also =
GUI Category, Internal_gui
