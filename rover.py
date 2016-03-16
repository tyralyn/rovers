import numpy
import math

def rotationMatrix(theta):
	return (numpy.matrix([[int(numpy.cos(theta)), -int(numpy.sin(theta))],[int(numpy.sin(theta)), int(numpy.cos(theta))]]))

class rover:
	leftRotMatrix = rotationMatrix(-math.pi/2)
	rightRotMatrix = rotationMatrix(math.pi/2)
	directions = {(0,1): 'N', (1,0): 'E', (0,-1): 'S', (-1,0): 'W'}
	def __init__(self,i,j, d):
		self.pos=numpy.matrix([i,j])
		self.ori=numpy.matrix([0,1])
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
	def getDirection(self):
		dirTuple=(self.ori.item(0), self.ori.item(1))
		return self.directions[dirTuple]
	def printRover(self):
		print('{} {} {}'.format(self.pos.item(0),self.pos.item(1),self.getDirection()))