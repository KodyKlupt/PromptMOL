# Edit Keys

### EDITING KEYS
 These are defaults, which can be redefined.  Note that while
 entering text on the command line, some of these control keys take on
 text editing functions instead (CTRL - A, E, and K, and DELETE), so
 you should clear the command line before trying to edit atoms.

#### ATOM REPLACEMENT
   CTRL-C    Replace picked atom with carbon   (C)
   CTRL-N    Replace picked atom with nitrogen (N)
   CTRL-O    Replace picked atom with oxygen   (O)
   CTRL-S    Replace picked atom with sulpher  (S)
   CTRL-G    Replace picked atom with hydrogen (H)
   CTRL-F    Replace picked atom with fluorene (F)
   CTRL-L    Replace picked atom with chlorine (Cl)
   CTRL-B    Replace picked atom with bromine  (Br)
   CTRL-I    Replace picked atom with iodine   (I)

#### ATOM MODIFICATION
   CTRL-J    Set charge on picked atom to -1
   CTRL-K    Set charge on picked atom to +1
   CTRL-D    Remove atom or bond (DELETE works too).
   CTRL-Y    Add a hydrogen to the current atom
   CTRL-R    Adjust hydrogens on atom/bond to match valence.
   CTRL-E    Inverts the picked stereo center, but you must first
             indicate the constant portions with the (lb) and (rb)
             selections.

   CTRL-T    Connect atoms in the (lb) and (rb) selections.
   CTRL-W    Cycle the bond valence on the picked bond.

UNDO and REDO of conformational changes (not atom changes!)

   CTRL-Z    undo the previous conformational change.
             (you can not currently undo atom modifications).
   CTRL-A    redo the previous conformational change.
