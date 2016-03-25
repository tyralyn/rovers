README

==================================

BUILD/RUN INFO
required packages:
 * re
 * numpy
 * math
 * sys

 To run, call 

 python __init__.py

==================================

ASSUMPTIONS:

The following assumptions are made:

That two multiple rovers cannot occupy the same space/coordinate. If two rovers are initialized to the same initial coordinate, only one will be added. 

That a rover will not fall off the edge of the plateau. It can be at the edge of the plateau, but will not fall off and will instead stay in the same place until a valid move (one that doesn't result in it falling off the plateau) is made. 

That a rover that does not start on the plateau will not be able to get on the plateau. A rover that does not start on the plateau will be ignored. 

As mentioned in the project description, the rovers are moved sequentially. 
