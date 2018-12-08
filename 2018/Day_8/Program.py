#!/usr/bin/env python#
import Common
from collections import defaultdict

def processNode(index, numbers, metaData, coordNum):
       if(index >= len(numbers)):
              return index, coordNum
       childNum = numbers[index]
       metaDataNum = numbers[index + 1]
       
       index += 2
       newCoordNum = coordNum
       for i in range(childNum):
              index, newCoordNum = processNode(index, numbers, metaData, newCoordNum + 1 )
       
       for i in range(metaDataNum):      
              metaData[coordNum] += numbers[index]
              index += 1
              
       return index, newCoordNum

def part1(input):
       numbers = Common.numbers(input)
       
       metaData = defaultdict(int)

       processingStack = []
       coordNum = 1
       index = 0
       
       processNode(index, numbers, metaData, coordNum)
       
       return sum(metaData.values())
       
def getNodeValue(index, numbers, metaData, coordNum):
       if(index >= len(numbers)):
              print("FaILURE")
              return None
       childNum = numbers[index]
       metaDataNum = numbers[index + 1]
       
       index += 2
       children = defaultdict(int)
       for i in range(childNum):
              (children[i + 1], index, coordNum) = getNodeValue(index, numbers, metaData, coordNum + 1 )
       
       metaData = []
       for i in range(metaDataNum):
              metaData.append(numbers[index])
              index += 1
       if(children):
              return (sum([children[ref] for ref in metaData if ref in children]), index, coordNum)
       else:
              return (sum(metaData), index, coordNum)

def part2(input):
       numbers = Common.numbers(input)
       
       metaData = defaultdict(int)

       processingStack = []
       coordNum = 1
       index = 0
       
       return getNodeValue(index, numbers, metaData, coordNum)[0]
              
              
input = Common.inputAsString()

print(part1(input))
print(part2(input))




