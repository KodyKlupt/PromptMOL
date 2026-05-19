# Python

Issuing the **Python** command will put you into a stateful pseudo-interactive Python session.  Or, more simply it's stateful in that you can invoke the Python session write some code, end the session, then restart the session and your data will be saved (see Example 1).  It's pseudo-interactive in that you don't get feedback until you type "python end," upon which your code is run the output appears.

This is a helpful command for testing different scripting or state-editing strategies for movie making.

##  USAGE
```python
1. start the session
python

1. ...
1. your Python code goes here
1. ...

1. end the session
python end
```



##  EXAMPLES
- Start the session.  Set x to 10.  End the session.  Restart the session and see if the value of x is recalled.

```python
python
x = 10
print(x)
python end
```

```python
python
print(x)
python end
```

Output:
 10

##  Python Version
Python scripts and commands used within PyMOL can only be written using the current version of Python that is supported by your version of PyMOL. To determine which version of Python you can use, type the following command into PyMOL:

```python
print(sys.version)
```

Note that this version of Python is not necessarily related to the version that you may have installed on your system.

This command can also be used to ensure that code you are distributing can be supported by the user's system.
