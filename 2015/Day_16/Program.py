import Common
import re

class Sue:
	def __init__(self, num):
		self.num = num
		self.compounds = {}
		
	def addCompound(self, compound, amount):
		self.compounds[compound] = amount
		
	def matchesCompound(self, compound, amount):
		return not (compound in self.compounds and self.compounds[compound] != amount)
		
	def matchesCompound2(self, compound, amount):
		if(compound not in self.compounds):
			return True
		if(compound == "cats" or compound == "trees"):
			return self.compounds[compound] > amount
		elif(compound == "pomeranians" or compound == "goldfish"):
			return self.compounds[compound] < amount
			
		return not (compound in self.compounds and self.compounds[compound] != amount)
		
	def matchesCompounds(self, compounds):
		if(len(self.compounds) == 0):
			return False
		for compound, amount in compounds.items():
			if(not self.matchesCompound2(compound, amount)):
				return False
		return True

def parseValue(compoundValue):
	values = compoundValue.strip().split(":")
	compound = values[0]
	amt = int(values[1].strip())
	return compound, amt
	
def parseSue(line):
	words = line.split()
	num = words[1].strip(":")
	line2 = re.sub("Sue [0-9]+:", "", line)
	compoundValues = line2.split(",")
	
	sue = Sue(num)
	for value in compoundValues:
		compound, amt = parseValue(value)
		sue.addCompound(compound, amt)
	
	return sue
		
def findSue(input):
	matchingCompound = { 
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1 }
	
	for line in input:
		sue = parseSue(line)
		if(sue.matchesCompounds(matchingCompound)):
			return sue.num
	print("2")
	return None
		
		


input = Common.inputAsLines()
print(findSue(input))
