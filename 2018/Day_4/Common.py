import re
def fileAsString(filename):
	file = open(filename)
	return file.read()

def fileAsLines(filename):
	file = open(filename)
	return file.readlines()

def inputAsString():
	file = open("Input.txt")
	return file.read()
	
def inputAsLines():
	file = open("Input.txt")
	return file.read().splitlines()

def inputAsNumericLines():
	file = open("Input.txt")
	return file.read().splitlines()
    
def sub(line):
    return re.sub('[^0-9]', ' ', line)