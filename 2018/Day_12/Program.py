#!/usr/bin/env python3#
import Common
import re
from collections import defaultdict

def getPlantAtIndex(plantArray, index):
       if(index not in plantArray):
              return "."
       return plantArray[index]
       
def getNewPlant(plantArray, patterns, index):
       plants = [getPlantAtIndex(plantArray, num) for num in range(index - 2, index + 3)]
       pattern = "".join(plants)
       if(pattern in patterns):
              return patterns[pattern]
       else:
              return "."
       

def assignNewPlant(newGen, oldGen, patterns, index):
       newGen[index] = getNewPlant(oldGen, patterns, index )

def printPlantArray(plantArray, gen):
       print("Gen:" + str(gen))
       for i in range(0,max(plantArray)):
              print(getPlantAtIndex(plantArray, i), end = "")
       print("")
	   
def sumTotalPlants(plantArray):
	   return sum(key for key,value in plantArray.items() if value =="#")
	   
def part1(input):
	isInitial = True
	plantArray = defaultdict(str)
	patterns = defaultdict(str)
	for line in input:
		if(isInitial):
			initialPlants = re.sub("[^#.]", "", line)
			plantArray = {item[0]:item[1] for item in zip(range(len(initialPlants)), initialPlants) }
			isInitial = False
		else:
			patternPair = line.strip().split('=>')
			pattern = patternPair[0].strip()
			result = patternPair[1].strip()
			patterns["".join(pattern)] = result
	printPlantArray(plantArray, 0)
	minPlant = 0
	maxPlant = len(plantArray) - 1
	initialPlantArray = {}
	initialPlantArray.update(plantArray)
	
	cycle = None
	totalPlants = sumTotalPlants(plantArray)
	lastTotalDiff = None
	repeatingGen = None
	totalAtRepeat = None
	for i in range(1, 5000):
		nextGen = defaultdict(str)
		
		assignNewPlant(nextGen, plantArray, patterns, minPlant - 1)
		assignNewPlant(nextGen, plantArray, patterns, minPlant - 2)
		assignNewPlant(nextGen, plantArray, patterns, maxPlant + 1)
		assignNewPlant(nextGen, plantArray, patterns, maxPlant + 2)
		
		for j in plantArray:
			assignNewPlant(nextGen, plantArray, patterns, j)
			
		plantArray = nextGen
		minPlant = minPlant - 2
		maxPlant = maxPlant + 2

		oldTotal = totalPlants
		totalPlants = sumTotalPlants(plantArray)
		
		totalDiff = totalPlants - oldTotal
		print(totalDiff)
		if totalDiff == lastTotalDiff:
			repeatingGen = i
			totalAtRepeat = totalPlants
			break
		lastTotalDiff = totalDiff
	
	return totalAtRepeat + totalDiff * (50000000000 - repeatingGen)
            
input = Common.inputAsLines()
#input = Common.inputAsString()

print(part1(input))
#print(part2(input))




