import rover
import bijectmap
import sys
import re

class platform:
	dirMap = bijectmap.bijectmap()
	def __init__(self,x,y):
		self.dirMap.addDict({(0,1):'N', (1,0):'E', (0,-1):'S', (-1,0):'W'})
		self.xMax = x
		self.yMax = y
		self.yMin = 0
		self.xMin = 0 
		self.rovers=[]
	def getRoverDirection(self, r):
		dirTuple=(r.getOri().item(0), r.getOri().item(1))
		return self.dirMap.get(dirTuple)

	def printRover(self, r):
		print('{} {} {}'.format(r.getX(),r.getY(),self.getRoverDirection(r)))

	def roverAtEdge(self, r):
		roverDir = self.getRoverDirection(r)
		if roverDir == 'N':
			return self.yMax <= r.getY() 
		elif roverDir == 'E':
			return self.xMax <= r.getX() 
		elif roverDir == 'S':
			return self.yMin >= r.getY()
		else: #wPossible = roverDir == 'W'
			return self.xMin >= r.getX()

	def roverOnPlatform(self,r):
		abovePlat = self.yMax < r.getY() 
		rightOfPlat = self.xMax < r.getX() 
		belowPlat = self.yMin > r.getY() 
		leftOfPlat = self.xMin > r.getX()
		return not (abovePlat or rightOfPlat or belowPlat or leftOfPlat)


	def addRover(self,i,j,d,s):
		r=rover.rover(i,j, d,s)
		if self.roverOnPlatform(r):
			self.rovers.append(r)

	def checkRoverMoves(self,s):
		m = re.match("^[LRM]*$", s)
		return m is not True
		
	def deployRover(self,r):
		moves = list(r.moves)
		for move in moves:
			if move == 'L':
				r.turnLeft()
			elif move == 'R':
				r.turnRight()
			elif move == 'M':
				if not self.roverAtEdge(r):
					r.moveForward()
			else:
				return

	def printRovers(self):
		for r in self.rovers:
			self.deployRover(r)
			self.printRover(r)


def main():
	p=None
	message = sys.stdin.readlines()
	#handle first line of input
	inp = message[0]
	inpList = inp.split()
	if len(inpList)!=2:
		print("invalid input: first line should consist of two integers")
		return
	else:
		validFirstInp = str(inpList[0]).isdigit()
		validSecondInp = str(inpList[1]).isdigit()
		if not ( validFirstInp and validSecondInp):
			print("invalid input: first line should consist of two integers")
			return
		else:
			p = platform(int(inpList[0]), int(inpList[1]))

	for i in range (1, len(message), 2):
		try:
			roverInfoList= message[i].split()
			if len(roverInfoList)!=3:
				print("invalid input: first line should consist of two integers and one of the following (N,S,E,W) to indicate direction")
				return
			else:
				validFirstInp = str(roverInfoList[0]).isdigit()
				validSecondInp = str(roverInfoList[1]).isdigit()
				validThirdInp = True if p.dirMap.get(roverInfoList[2]) != None else False
				if not (validFirstInp and validSecondInp and validThirdInp):
					print("invalid input: first line should consist of two integers and one of the following (N,S,E,W) to indicate direction")
					return
				else:
					roverMoves=message[i+1].strip()
					if p.checkRoverMoves(roverMoves):
						p.addRover(int(roverInfoList[0]), int(roverInfoList[1]), p.dirMap.get(str(roverInfoList[2])) , roverMoves)
					else:
						print ("invalid input: only valid moves are L (left turn), R (right turn), and M (move forward)")
						return	
		except IndexError:
			print("invalid input: must have list of moves after declaring a rover")
			return
	p.printRovers()

main()
