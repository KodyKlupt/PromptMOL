# Mset

- *mset** sets up a relationship between molecular states and movie frames.  This makes it possible to control which states are shown in which frame.

The related command **madd** appends to the end of a movie. It is identical to the **mset** command, except for the default value of the **frame** argument (0 instead of 1).

##  Usage
 mset specification [, frame ]
 madd specification [, frame ]

##  Arguments
- **specification** = str: state sequence (see below for syntax), or empty string to delete movie {default: }
- **frame** = int: start frame, or 0 to append to the end of an existing movie {default: 1 (0 for madd)}

##  Specification Syntax
The state sequence specification consists of numbers, and the operators "x" and "-". Spaces between operators are optional.

Operator semantic:

- *state* **x** *count*: Repeat state *state* for *count* frames
- *state1* **-** *state2*: Iterate from *state1* to *state2*, yields *abs(state1 - state2) + 1* frames

Formal syntax description:

- *specification* ::= *state* [**x** *count*] {**-** *specification*} [*specification*]
- *state* ::= **number**
- *count* ::= **number**

##  Examples
```python
mset 1         # simplest case, one state -> one frame
mset 1 x10     # ten frames, all corresponding to state 1
mset 1 1 1 1 1 1 1 1 1 1 # identical to previous
mset 1-20      # map a 20 state trajectory to 20 frames
mset 1 2 3 4 5-20 # identical to previous

mset 1 x30 1 -15 15 x30 15 -1
1. more realistic example:
1. the first thirty frames are state 1
1. the next 15 frames pass through states 1-15
1. the next 30 frames are of state 15
1. the next 15 frames iterate back to state 1
```

```python
mset 1 x200 -78 -2 -78 -2 -78 x200 79 -156 157 x200 -234 235 x400
1. mset 1 x200 makes the first state last for 200 frames
1. -78 -2 takes us FROM state 1 to 78, then back to frame 2.  I've repeated this for dramatic effect.
1. Then we pause at 78 for 200 frames, then go from 79-156 and pause at 157 for 200 frames, etc.
```

```python
cmd.mset("1 -%d" % cmd.count_states())
1. this will create a one-to-one mapping of states to movie frames. useful for making movies from trajectory files.
```

##  PyMOL API
```python
cmd.mset(string specification, int frame=1)
cmd.madd(string specification, int frame=0)
```
