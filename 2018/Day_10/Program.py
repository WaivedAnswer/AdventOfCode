#!/usr/bin/env python3#
import Common
from collections import defaultdict

def draw(drawMap, time, minX, minY, maxX, maxY):
       print("Time: " + str(time) + '-' * 50)
       for i in range(minY, maxY + 1):
              for j in range(minX, maxX + 1):
                     if(i in drawMap and j in drawMap[i]):
                            print(drawMap[i][j], end = "")
                     else:
                            print(".", end="")
              print("")
       print("")

def moveCoord(coord, time):
       coordX = coord[0]
       coordY = coord[1]
       velX = coord[2]
       velY = coord[3]
       return (coordX + time*velX, coordY + time*velY)
       
def drawCoords(coords, time):
       drawMap = defaultdict(lambda: defaultdict(None))
       
       minX = 9999999
       minY = 9999999
       maxX = -9999999
       maxY = -9999999
       for coord in coords:
              newCoord = moveCoord(coord, time)
              drawMap[newCoord[1]][newCoord[0]] = "#"
              minX = min(minX, newCoord[0])
              minY = min(minY, newCoord[1])
              maxX = max(maxX, newCoord[0])
              maxY = max(maxY, newCoord[1])
              
       if(abs(maxX - minX) < 75 and abs(maxY - minY) < 75):
              draw(drawMap, time, minX, minY, maxX, maxY)
       
def part1(input):
       coords = []
       for line in input:
              coordX, coordY, velX, velY = Common.numbers(line)
              coords.append((coordX,coordY,velX, velY))
              
       for i in range(100000):
              drawCoords(coords, i)
       return 0
            
input = Common.inputAsLines()
print(part1(input))




