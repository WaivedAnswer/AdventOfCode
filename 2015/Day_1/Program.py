

def parseInput(filename):
	file = open(filename)
	return file.read()
def traverseFloors(bracketStrings):
	floor = 0
	for c in bracketStrings:
		if(c == "("):
			floor += 1
		elif(c == ")"):
			floor -= 1 
	print(floor)
	
def traverseFloorsToBasement(bracketStrings):
	floor = 0
	for i, c in enumerate(bracketStrings):
		if(c == "("):
			floor += 1
		elif(c == ")"):
			floor -= 1
		if(floor == -1):
			print(i+1)
		
input = parseInput("input.txt")
traverseFloors(input)
traverseFloors("(())")
traverseFloors("()()")
traverseFloors("(((")
traverseFloors("(()(()(")
traverseFloors("))(((((")
traverseFloors("())")
traverseFloors("))(")
traverseFloors(")))")
traverseFloors(")())())")

traverseFloorsToBasement(input)