import sys
import platform
import errorstrings

def main():
	p=None
	message = sys.stdin.readlines()
	#handle first line of input
	inp =""
	try: 
		inp = message[0]
	except IndexError:
		print(errorstrings.emptyFileError)
		return

	#handle subsequent input	
	inpList = inp.split()
	#only one line of input present
	if len(inpList)!=2:
		print(errorstrings.plateauDeclarationError.format(0))
		return
	else:
		#check validity of inputs for plateau declaration 
		validFirstInp = str(inpList[0]).isdigit()
		validSecondInp = str(inpList[1]).isdigit()
		if not ( validFirstInp and validSecondInp):
			print(errorstrings.plateauDeclarationError.format(0))
			return
		else:
			p = platform.platform(int(inpList[0]), int(inpList[1]))

	for i in range (1, len(message), 2):
		try:
			roverInfoList= message[i].split()
			#if no rovers are declared
			if len(roverInfoList)!=3:
				print(errorstrings.roverDeclarationError.format(i))
				return
			else:
				validFirstInp = str(roverInfoList[0]).isdigit()
				validSecondInp = str(roverInfoList[1]).isdigit()
				validThirdInp = True if p.dirStringToTuple.get(roverInfoList[2]) != None else False
				if not (validFirstInp and validSecondInp and validThirdInp):
					print(errorstrings.roverDeclarationError.format(i))
					return
				else:
					if message[i+1].isspace():
						print(errorstrings.roverMovesNeededError.format(i))
						return
					roverMoves=message[i+1].strip()
					if p.checkRoverMoves(roverMoves):
						p.addRover(int(roverInfoList[0]), int(roverInfoList[1]), str(roverInfoList[2]) , roverMoves)
					else:
						print (errorstrings.roverMovesError.format(i))
						return	
		except IndexError:
			print(errorstrings.roverMovesNeededError.format(i))
			return
	p.deployAndPrintRovers()

main()