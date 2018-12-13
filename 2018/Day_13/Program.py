#!/usr/bin/env python3#
import Common
from collections import defaultdict
from enum import Enum

class Turns(Enum):
       LEFT = 0
       STRAIGHT = 1
       RIGHT = 2
       
turnOrder = [Turns.LEFT, Turns.STRAIGHT, Turns.RIGHT]
       
cartDirections = ["<", "^", ">", "v"]
straights = ["|", "-"]
curves = ["/", "\\"]
intersection = "+"

def getIntersectionDirection(currDirection, lastTurnIndex):
       if(lastTurnIndex == None):
              nextIndex = 0
       else:
              nextIndex = (lastTurnIndex + 1) % len(turnOrder)
              
       turn = turnOrder[nextIndex]
       
       if(turn == Turns.STRAIGHT):
              return currDirection, nextIndex
       elif(turn == Turns.LEFT):
              return cartDirections[(cartDirections.index(currDirection) - 1) % len(cartDirections)], nextIndex
       elif(turn == Turns.RIGHT):
              return cartDirections[(cartDirections.index(currDirection) + 1) % len(cartDirections)], nextIndex
       
       return None
       
def getCurveDirection(currDirection, curve):
       if(currDirection == "^" or currDirection == "v"):
              if(curve == "\\"):
                     return cartDirections[(cartDirections.index(currDirection) - 1) % len(cartDirections)]
              elif(curve == "/"):
                     return cartDirections[(cartDirections.index(currDirection) + 1) % len(cartDirections)]
       else:
              if(curve == "\\"):
                     return cartDirections[(cartDirections.index(currDirection) + 1) % len(cartDirections)]
              elif(curve == "/"):
                     return cartDirections[(cartDirections.index(currDirection) - 1) % len(cartDirections)]
       
       return Nones
       
def getCartMovePos(row,col,currDirection,lastTurnIndex, coords):
       
       if(currDirection == "<"):
              col -= 1
       elif(currDirection == ">"):
              col += 1
       elif(currDirection == "^"):
              row -=1
       else:
              row +=1
              
       if(coords[row][col] in straights):
              return (row,col,currDirection,lastTurnIndex)
       elif(coords[row][col] == intersection):
              newDirection, newTurnIndex = getIntersectionDirection(currDirection, lastTurnIndex)
              return (row,col, newDirection, newTurnIndex)
       elif(coords[row][col] in curves):
              newDirection = getCurveDirection(currDirection, coords[row][col])
              return (row,col, newDirection, lastTurnIndex)
       
       return row,col,currDirection,lastTurnIndex
       
def printGrid(coords, carts):
       for i in range(len(coords)):
              for j in range(len(coords[i])):
                     if((i,j) in carts):
                            print(carts[(i,j)][0], end="")
                     else:
                            print(coords[i][j], end = "")
              print("")
       
def part1(input):
       coords = []
       carts = defaultdict(tuple)
       
       for i,line in enumerate(input):
              coords.append([])
              for j,c in enumerate(line):
                     if(c in cartDirections):
                            carts[(i,j)] = (c, None)
                            if(c == "^" or c=="v"):
                                   coords[i].append("|")
                            else:
                                   coords[i].append("-")
                     else:
                            coords[i].append(c)
                         
                         
       ticks = 0
       crash = None
       while(not crash):
              newCarts = defaultdict(tuple)
              for cartPos,cart in sorted(carts.items(), key=lambda item: item[0][0]*len(coords) + item[0][1]):
                     #print(cartPos, cart)
                     row, col, direction, lastTurnIndex = getCartMovePos(cartPos[0], cartPos[1], cart[0], cart[1], coords)
                     if((row,col) in newCarts):
                            crash = (col,row)
                            break
                     newCarts[(row,col)] = (direction, lastTurnIndex)
              carts = newCarts
              ticks += 1
              printGrid(coords,carts)

       return crash
            
input = Common.inputAsLines()
#input = Common.inputAsString()

print(part1(input))
#print(part2(input))




