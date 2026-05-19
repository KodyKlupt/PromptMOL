# Mview

The mview command can store and delete movie keyframes.

Keyframes store a view (camera or object position) and optionally the object state and/or a scene. Between keyframes, PyMOL will interpolate views and states, allowing for smooth animations.

Before using mview, the movie timeline has to be set up with mset.

##  Usage
 mview [ action [, first [, last [, power [, bias
     [, simple [, linear [, object [, wrap [, hand
     [, window [, cycles [, scene [, cut [, quiet
     [, auto [, state [, freeze ]]]]]]]]]]]]]]]]]]

##  Arguments
- **action** = str: one of store, clear, reset, purge, interpolate, uninterpolate, reinterpolate, toggle, toggle_interp, smooth {default: store}
- **first** = int: frame number or 0 for current frame {default: 0}
- **power** = float: slow down animation at keyframe (0.0) or not (1.0) {default: 0.0}
- **object** = str: name of object for object keyframes, or empty for global (camera) keyframes {default: }
- **scene** = str: name of scene to store scene with key frame {default: }
- **cut** = float 0.0-1.0: scene switch moment (0.0: beginning of transition, 1.0: end of transition) {default: 0.5}
- **auto** = -1/0/1: if freeze=0, then auto reinterpolate after store, clear, or toggle {default: -1 = use movie_auto_interpolate}
- **state** = int: if > 0, then store object state {default: 0}
- **freeze** = 0/1: never auto reinterpolate {default: 0}

##  Examples
###  Ligand zoom
 fetch 1rx1, async=0
 as cartoon
 as sticks, organic
 mset 1x70
 orient
 mview store, 1
 mview store, 70
 orient organic
 mview store, 30
 mview store, 40
 mplay

###  360° rotation
 fragment ala
 mset 1x90
 mview store, 1
 mview store, 90
 turn y, 120
 mview store, 30, power=1.0
 turn y, 120
 mview store, 60, power=1.0
 mplay

###  360° rotation of a single object
 set movie_auto_store, 0
 fragment ala
 fragment his
 translate [10, 0, 0], his
 zoom
 mset 1x90
 mview store, 1, object=his
 mview store, 90, object=his
 rotate y, 120, object=his  # keyword >>object<< is absolutely necessary! Otherwise movie will not work.
 mview store, 30, power=1.0, object=his
 rotate y, 120, object=his
 mview store, 60, power=1.0, object=his
 mplay

###  Object-level state-sweep
 load http://pymol.org/tmp/morph.pdb.gz
 dss
 as cartoon
 mset 1x80
 mview store, 1, object=m, state=1
 mview store, 30, object=m, state=30
 mview store, 50, object=m, state=30
 mview store, 80, object=m, state=1
 mplay

###  Ligand binding
 set movie_auto_store, 0
 fetch 1rx1, async=0
 extract ligand, organic
 as cartoon, 1rx1
 as sticks, ligand
 set_view (\
   0.527486444, -0.761115909, -0.377440333,\
   0.736519873, 0.631122172, -0.243357301,\
   0.423434794, -0.149625391, 0.893482506,\
   0.000059791, -0.000049331, -140.287048340,\
   34.670463562, 51.407436371, 17.568315506,\
   111.284034729, 169.290832520, -19.999998093 )
 mset 1x60
 mview store, 60, object=ligand
 translate [10, 0, 0], object=ligand
 mview store, 1, object=ligand
 mplay

###  Scene based movie
 fragment ala
 as sticks
 color blue
 scene bluesticks, store
 as spheres
 color red
 turn y, 180
 scene redspheres, store
 mset 1x60
 mview store, 1, scene=bluesticks
 mview store, 30, scene=redspheres
 mplay
