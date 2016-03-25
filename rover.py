import numpy
import math

##################################################
#                                                #
#   Class that holds info on rovers.             #
#   Holds position and orientation of rovers     #
#   and string that contains rover's moves.      #
#   Moves are stored as a string, but they are   #
#   checked before the rover is made.            #
#                                                #
##################################################

class rover:
	leftRotMatrix = (numpy.matrix([[int(numpy.cos(-math.pi/2)), -int(numpy.sin(-math.pi/2))],[int(numpy.sin(-math.pi/2)), int(numpy.cos(-math.pi/2))]])) 
	rightRotMatrix = (numpy.matrix([[int(numpy.cos(math.pi/2)), -int(numpy.sin(math.pi/2))],[int(numpy.sin(math.pi/2)), int(numpy.cos(math.pi/2))]])) 

	#takes as input coordinates of rover (i,j) , tuple of direction, and string of moves
	def __init__(self,xCoord,yCoord,orientation,moves):
		self.pos=numpy.matrix([xCoord,yCoord])
		self.ori=numpy.matrix(orientation)
		self.moves = moves

	#return the next position that the rover would move, but do not move it
	def peekForwardX(self):
		return (self.pos+self.ori).item(0)
	def peekForwardY(self):
		return (self.pos+self.ori).item(1)

	#maintains orientation of rover, but moves it forward
	def moveForward(self):
		self.pos=self.pos+self.ori
	#modify the orientation of the rover to turn it left
	def turnLeft(self):
		self.ori=self.ori*self.leftRotMatrix
	#modify the orientation of the rover to turn it right	
	def turnRight(self):
		self.ori=self.ori*self.rightRotMatrix

	#getters for x-coordinate and y-coordinates of rover position and orientation
	def getPosX(self):
		return self.pos.item(0)
	def getPosY(self):
		return self.pos.item(1)
	def getOriX(self):
		return self.ori.item(0)
	def getOriY(self):
		return self.ori.item(1)

