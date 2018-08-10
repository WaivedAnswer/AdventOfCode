def fileAsString(filename):
	file = open(filename)
	return file.read()

def fileFromLines(filename):
	file = open(filename)
	return file.readlines()

def inputAsString():
	file = open("Input.txt")
	return file.read()
	
def inputFromLines():
	file = open("Input.txt")
	return file.read()