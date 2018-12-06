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
	
def numbers(line):
	return [int(numstr) for numstr in re.sub("[^0-9]", " ", line).split()]
	
def maxValuePair(dictionary):
	return max(dictionary.items(), key=lambda x:x[1])
    
def sub(line):
    return re.sub('[^0-9]', ' ', line)