def fileAsString(filename):
	file = open(filename)
	return file.read()

def fileAsLines(filename):
	file = open(filename)
	return file.read().splitlines()

def inputAsString():
	file = open("Input.txt")
	return file.read()
	
def inputAsLines():
	file = open("Input.txt")
	return file.read().splitlines()