import rover

class platform:
	validDirections = ['N','E','S','W']
	def __init__(self,x,y):
		self.xMax = x
		self.yMax = y
		self.yMin = 0
		self.xMin = 0 
		self.rovers=[]
	def roverAtEdge(self, r):
		roverDir = r.getDirection()
		if roverDir == 'N':
			return self.yMax <= r.getY() 
		elif roverDir == 'E':
			return self.xMax <= r.getX() 
		elif roverDir == 'S':
			return self.yMin >= r.getY()
		else: #wPossible = roverDir == 'W'
			return self.xMin >= r.getX()
	def addRover(self,i,j,d,s):
		r=rover.rover(i,j, d)
		moves = list(s)
		for move in moves:
			if move == 'L':
				r.turnLeft()
			elif move == 'R':
				r.turnRight()
			elif move == 'M':
				if not self.roverAtEdge(r):
					r.moveForward()
			else:
				print ("invalid input: only valid moves are L (left turn), R (right turn), and M (move forward)")

	def printRovers(self):
		for rover in rovers:
			rover.printRover()


def main():
	p=None
	#handle first line of input
	inp = input()
	while inp!= "":
		inpList = inp.split()
		if len(inpList)!=2:
			print("invalid input: first line should consist of two integers")
		else:
			validFirstInp = str(inpList[0]).isdigit()
			validSecondInp = str(inpList[1]).isdigit()
			if not ( validFirstInp and validSecondInp):
				print("invalid input: first line should consist of two integers")
			else:
				p = platform(int(inpList[0]), int(inpList[1]))
				break;
		inp = input()

	inp = input()
	while inp!= "":
		while inp!="":
			inpList = inp.split()
			if len(inpList)!=3:
				print("invalid input: first line should consist of two integers and one of the following (N,S,E,W) to indicate direction")
			else:
				validFirstInp = str(inpList[0]).isdigit()
				validSecondInp = str(inpList[1]).isdigit()
				validThirdInp = True if inpList[2] in p.validDirections else False
				if not (validFirstInp and validSecondInp and validThirdInp):
					print("invalid input: first line should consist of two integers and one of the following (N,S,E,W) to indicate direction")
				else:
					inp = input()
					p.addRover(int(inpList[0]), int(inpList[1]), inpList[2], inp)
			inp = input()


main()
