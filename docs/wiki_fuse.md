# Fuse

- *fuse** joins two objects into one by forming a bond.  A copy of
the object containing the first atom is moved so as to form an
approximately reasonable bond with the second, and is then merged
with the first object.

##  Usage
 fuse [ selection1 [, selection2 [, mode [, recolor [, move ]]]]]

##  Arguments
- selection1 = str: single atom selection (will be copied to object 2) {default: (pk1)}
- selection2 = str: single atom selection {default: (pk2)}
- mode = int: {default: 0}
- * mode=0:
- * mode=1: adopt segi/chain/resn`resi
- * mode=2: adopt segi/chain
- * mode=3: don't move and don't create a bond, just combine into single object
- recolor = bool: recolor C atoms to match target {default: 1}
- move = bool: {default: 1}

##  Example
Phosphorylate a serine residue:

 fetch 1ubq, async=0

 fragment phosphite
 remove phosphite & elem H

 fuse phosphite & elem P, /1ubq///65/OG, mode=1
 delete phosphite

 show sticks, resi 65
 orient resi 65
 unpick
