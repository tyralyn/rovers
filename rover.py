import numpy
import math

################################################
#  class that holds info on rovers             #
#  holds position and orientation of rovers    #
#  and string that contains rover's moves.     #
#  moves are stored as a string, but they are  #
#  checked before the rover is made            #
################################################

def rotationMatrix(theta):
	return (numpy.matrix([[int(numpy.cos(theta)), -int(numpy.sin(theta))],[int(numpy.sin(theta)), int(numpy.cos(theta))]]))

class rover:
	leftRotMatrix = rotationMatrix(-math.pi/2)
	rightRotMatrix = rotationMatrix(math.pi/2)

	#takes as input coordinates of rover (i,j) , tuple of direction
	def __init__(self,i,j, d, s):
		self.pos=numpy.matrix([i,j])
		self.ori=numpy.matrix(d)
		self.moves = s
	def peekForward(self):
		return (self.pos+self.ori)
	def moveForward(self):
		self.pos=self.peekForward()
	def turnLeft(self):
		self.ori=self.ori*self.leftRotMatrix
	def turnRight(self):
		self.ori=self.ori*self.rightRotMatrix
	def getX(self):
		return self.pos.item(0)
	def getY(self):
		return self.pos.item(1)
	def getOri(self):
		return self.ori

