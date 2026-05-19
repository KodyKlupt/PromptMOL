# All states

## Overview
When set "on", this setting causes PyMOL to display all states or in NMR jargon: all the models in the ensemble.
The 'default' behavior (OFF) can be overridden by placing the "set all_states, on" statement into your '.pymolrc' file, located in your login directory (under all flavors of unix).

## Syntax
```python
set all_states, on
set all_states, off
```

## Example
```python
1. fetch a PDB and show it in multiple states; this one
1. line does the work of the next 6 lines.
fetch 1nmr

1. this is older code, use the above code which is newer
import urllib2
pdbCode = '1BRV'
pdbUrl = 'http://www.rcsb.org/pdb/downloadFile.do?fileFormat=pdb&compression=NO&structureId='+pdbCode
pdbFile = urllib2.urlopen(pdbUrl)
pdbContent = pdbFile.read()
cmd.read_pdbstr(pdbContent, pdbCode)

set all_states, on
```

This shows the effect of turning on/off the **all_states** setting used with the script above.

Image:All_states_on.png|set all_states, on
Image:All_states_off.png|set all_states, off
