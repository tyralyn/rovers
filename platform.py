import rover
import bijectmap
import re

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
	#bijective mapping between direction strings and vector tuples
	dirMap = bijectmap.bijectmap()
	dirMap.addDict({(0,1):'N', (1,0):'E', (0,-1):'S', (-1,0):'W'})

	#takes dimensions of rectangular plateau
	def __init__(self,xCoord,yCoord):	
		self.xMax = xCoord
		self.yMax = yCoord
		self.yMin = 0
		self.xMin = 0 
		self.rovers=[]
		self.occupancy = [[ False for j in range(self.yMax+1)] for i in range(self.xMax+1)]
	
	#puts rover in rover list if it is on the plateau
	def addRover(self,i,j,d,s):
		r=rover.rover(i,j, d,s)
		if self.roverOnPlatform(r):
			self.rovers.append(r)
			self.occupyPosition(r)

	#regex matching of moves string to see whether all characters are valid moves
	def checkRoverMoves(self,s):
		m = re.match("^[LRM]*$", s)
		return m is not True

	#determine whether rover will move off the edge
	def roverAtEdge(self, r):
		roverDir = self.getRoverDirection(r)
		if roverDir == 'N':
			return self.yMax < r.peekForwardY() 
		elif roverDir == 'E':
			return self.xMax < r.peekForwardX() 
		elif roverDir == 'S':
			return self.yMin > r.peekForwardY()
		else: #roverDir == 'W'
			return self.xMin > r.peekForwardX()

	#determine whether rover is on the platform
	def roverOnPlatform(self,r):
		abovePlat = self.yMax < r.getPosY() 
		rightOfPlat = self.xMax < r.getPosX() 
		belowPlat = self.yMin > r.getPosY() 
		leftOfPlat = self.xMin > r.getPosX()
		return not (abovePlat or rightOfPlat or belowPlat or leftOfPlat)

	#determine whether the position that the rover wishes to occupy is occupied
	def positionOccupied(self,r):
		x = r.peekForwardX()
		y = r.peekForwardY()
		return self.occupancy[y][x]

	#have the rover occupy that position
	def occupyPosition(self,r):
		x = r.getPosX()
		y = r.getPosY()
		self.occupancy[y][x] = True
	
	#vacate a position
	def vacatePosition(self,r):
		x = r.getPosX()
		y = r.getPosY()
		self.occupancy[y][x] = False

	#if rover is not at an edge and not about to go to an occupied position
	#stop occupying the current position, move, and start occupying the next	
	def moveRover(self,r):
		if not self.roverAtEdge(r) and not self.positionOccupied(r):
			self.vacatePosition(r)
			r.moveForward()
			self.occupyPosition(r)

	#iterate through all moves in the move sequence and turn or move accordingly
	def deployRover(self,r):
		moves = list(r.moves)
		for move in moves:
			if move == 'L':
				r.turnLeft()
			elif move == 'R':
				r.turnRight()
			elif move == 'M':
				self.moveRover(r)
			else:
				pass

	#get the string direction value of a rover
	def getRoverDirection(self, r):
		dirTuple=(r.getOriX(), r.getOriY())
		return self.dirMap.get(dirTuple)

	#print the rover's position and orientation
	def printRover(self, r):
		print('{} {} {}'.format(r.getPosX(),r.getPosY(),self.getRoverDirection(r)))

	#iterate through rovers, deploying them and printing their position and orientation in sequence
	def evalRovers(self):
		for r in self.rovers:
			self.deployRover(r)
			self.printRover(r)


