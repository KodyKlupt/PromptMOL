# Auto zoom

## Overview
When set "on", this setting causes PyMOL to "auto_zoom" to any new object upon loading.  This is helpful when one wishes to look at a new object immediately upon loading it into your PyMOL session; it can also be vexing in the situation where you have a carefully constructed view that might be "lost" if you do not anticipate that the program will change the view on loading an additional object.  If you opt to use "auto_zoom on", it is also wise to get in the habit of frequent session saves and also use of "scenes" and the "get_view" utility, which will save one's current view orientation matrix to the (temporary) memory cache.  The 'default' behavior (ON) can be overridden by placing the "set auto_zoom, off" statement into your '.pymolrc' file, located in your login directory (under all flavors of unix).

## Syntax
set auto_zoom, on

set auto_zoom, off
