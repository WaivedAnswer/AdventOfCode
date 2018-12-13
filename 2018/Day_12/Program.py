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
       for i in range(-3,35):
              print(getPlantAtIndex(plantArray, i), end = "")
       print("")
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
       #printPlantArray(plantArray, 0)
       minPlant = 0
       maxPlant = len(plantArray) - 1
       initialPlantArray = {}
       initialPlantArray.update(plantArray)
       
       cycle = None
       
       for i in range(1, 50000000001):
              print(i)
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

              if(set(initialPlantArray.items()).issubset(set(plantArray.items()))):
                     cycle = i
                     break
                     
       print(cycle)
       plantArray = initialPlantArray
       for i in range(1, 50000000001 % cycle):
              print(i)
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
              
       totalPlants = sum(key for key,value in plantArray.items() if value =="#")
              
       return totalPlants
            
input = Common.inputAsLines()
#input = Common.inputAsString()

print(part1(input))
#print(part2(input))




