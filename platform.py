import rover
import re

maxOccupancyOfSpace = 1

##################################################
#                                                #
#   Platform that controls a system of rovers.   #
#   Controls rovers on rectangular plateau of    #
#   dimensions (x,y). Does not allow rovers to   #
#   fall off the plateau, and rovers that are    #
#   not originally placed on the plateau will    #
#   be ignored.                                  #
#                                                #
##################################################

class platform:
	#mapping between direction strings and vector tuples
	dirTupleToString = {(0,1):'N', (1,0):'E', (0,-1):'S', (-1,0):'W'}
	dirStringToTuple = { v:k for k,v in dirTupleToString.items()}

	#takes dimensions of rectangular plateau
	def __init__(self,xCoord,yCoord):	
		self.xMax = xCoord
		self.yMax = yCoord
		self.yMin = 0
		self.xMin = 0 
		self.rovers=[]
		self.occupancy = [[ 0 for j in range(self.yMax+1)] for i in range(self.xMax+1)]
	
	#puts rover in rover list if it is on the plateau
	def addRover(self,i,j,d,s):
		r=rover.rover(i,j, self.dirStringToTuple.get(d),s)
		if self.positionOnPlatform(i,j):
			if self.occupancy[j][i] < maxOccupancyOfSpace:
				self.rovers.append(r)
				self.occupancy[j][i] += 1

	#regex matching of moves string to see whether all characters are valid moves
	def checkRoverMoves(self,s):
		m = re.match("^[LRM]*$", s)
		return m is not True

	#determine whether rover is on the platform, returns true if
	def positionOnPlatform(self,x,y):
		abovePlat = self.yMax  < y 
		rightOfPlat = self.xMax < x 
		belowPlat = self.yMin > y 
		leftOfPlat = self.xMin > x
		return not (abovePlat or rightOfPlat or belowPlat or leftOfPlat)

	#if rover is not at an edge move forward
	def moveRover(self,r):
		x = r.peekForwardX()
		y = r.peekForwardY()
		if self.positionOnPlatform(x,y):
			if self.occupancy[y][x] < maxOccupancyOfSpace:
				r.moveForward()

	#get the string direction value of a rover
	def getRoverDirection(self, r):
		dirTuple=(r.getOriX(), r.getOriY())
		return self.dirTupleToString.get(dirTuple)

	#iterate through rovers, deploying them and printing their position and orientation in sequence
	def deployAndPrintRovers(self):
		for r in self.rovers:
			moves = list(r.moves)
			moved = False
			for move in moves:
				if move == 'L':
					r.turnLeft()
				elif move == 'R':
					r.turnRight()
				elif move == 'M':
					if not moved:
						self.occupancy[r.getPosY()][r.getPosX()]-=1
						moved = True
					self.moveRover(r)
				else:
					pass
			x = r.getPosX()
			y = r.getPosY()
			self.occupancy[y][x] += 1
			print('{} {} {}'.format(r.getPosX(),r.getPosY(),self.getRoverDirection(r)))


