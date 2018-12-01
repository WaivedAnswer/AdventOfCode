# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:56:51 2017

@author: WFN53616
"""
import math;
import numpy as np;

def CalcBottomRightRingNum(ringNum):
    return 1 + 4*(ringNum*(ringNum + 1));

def GetRingNum(num):
    ringNum = 0;
    while True:
        nextBottomRightNum = CalcBottomRightRingNum(ringNum);
        if(nextBottomRightNum >= num):
            break
        ringNum = ringNum + 1;
        
    return ringNum;

def GetDifferenceFromBottomRightRingNum(ringNum, num):
    return CalcBottomRightRingNum(ringNum) - num;

#measured from 1
def GetCoordinates(ringNum, diff):
    if(ringNum == 0):
        if(diff == 0):
            return (0,0);
        else:
            raise Exception("incorrect inputs");
    maxDiff = CalcBottomRightRingNum(ringNum) - CalcBottomRightRingNum(ringNum - 1);
    if(diff > maxDiff):
        print(maxDiff, diff)
        raise Exception("You cannot be on this ring")
    coordX = ringNum;
    coordY = ringNum;
    sideSteps = ringNum * 2;
    for i in range(diff):
        #left
        if(i/sideSteps == 0):
            coordX-=1;
        # up
        elif(i/sideSteps == 1):
            coordY-=1;
        #right
        elif(i/sideSteps == 2):
            coordX+=1;
        #down
        elif(i/sideSteps == 3):
            coordY+=1;
    coordinates = (coordX, coordY);
    return coordinates
        
        
    

def GetSpiralCoordinates(num):
    ringNum = GetRingNum(num);
    diff = GetDifferenceFromBottomRightRingNum(ringNum, num);
    return GetCoordinates(ringNum, diff);
    
def GetManhattanDistance(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1]);
    
def GetShortestPath(num):
    return GetManhattanDistance(GetSpiralCoordinates(num));
    
def SumAdjacents(coords, grid):
    sum = 0;
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            nextCoordX = coords[0] + i;
            nextCoordY = coords[1] + j;
            
            if((i == 0 and j == 0) or (abs(nextCoordX) > (len(grid) + 1)/2) or (abs(nextCoordY) > (len(grid[nextCoordX])+1)/2)):
                continue;
            sum += grid[nextCoordX][nextCoordY];
    return sum;
    
    
def GetFirstNumberOfSumSpiralGreaterThanNum(num):
    #spiral ring of this sum spiral is at least smaller than
    #the single counting version
    #except for first ring numbers
    #not accurate for numbers below 10
    #this is due to the adjacencies wrapping because my holding data structure is based from
     #top left instead of center = 0,0
    
    countingRingNum = GetRingNum(num);
    traverseFinish = num;
    if(num < 10):
        traverseFinish = 10;
        countingRingNum = GetRingNum(traverseFinish);
        
    dim = 1 + countingRingNum * 2;
    #start with grid of zeros
    
    grid = np.zeros((dim, dim));
    #[0][0] is 1. -coordinates should wrap
    grid[0][0] = 1;

    for i in range(1, traverseFinish):
        # + 1 to align with original spiral
        coords = GetSpiralCoordinates(i + 1);
        sum = SumAdjacents(coords, grid);
        if(sum > num):
            return sum;
        grid[coords[0]][coords[1]] = sum;
    
    return num;
    
    

print(GetFirstNumberOfSumSpiralGreaterThanNum(1) == 2);
print(GetFirstNumberOfSumSpiralGreaterThanNum(5) == 10);
print(GetFirstNumberOfSumSpiralGreaterThanNum(6)== 10);
print(GetFirstNumberOfSumSpiralGreaterThanNum(8)== 10);
print(GetFirstNumberOfSumSpiralGreaterThanNum(9)== 10);
print(GetFirstNumberOfSumSpiralGreaterThanNum(10)== 11);
"""print(GetFirstNumberOfSumSpiralGreaterThanNum(11) == 23);
print(GetFirstNumberOfSumSpiralGreaterThanNum(142) == 147);
print(GetFirstNumberOfSumSpiralGreaterThanNum(655) == 747);
print(GetFirstNumberOfSumSpiralGreaterThanNum(200) == 304);
print (GetDifferenceFromBottomRightRingNum( 0, 1) == 0);
print (GetDifferenceFromBottomRightRingNum(1, 9) == 0);
print (GetDifferenceFromBottomRightRingNum(2, 25) == 0);
print (GetDifferenceFromBottomRightRingNum(3, 49) == 0);
print (GetDifferenceFromBottomRightRingNum(4, 81) == 0);    

print (CalcBottomRightRingNum(0) == 1);
print (CalcBottomRightRingNum(1) == 9);
print (CalcBottomRightRingNum(2) == 25);
print (CalcBottomRightRingNum(3) == 49);
print (CalcBottomRightRingNum(4) == 81);
print (GetSpiralRing(1) == 0);
print (GetSpiralRing(2) == 1);
print (GetSpiralRing(5) == 1);
print (GetSpiralRing(9) == 1);
print (GetSpiralRing(15) == 2);
print (GetSpiralRing(25) == 2);
print (GetSpiralRing(35) == 3);
print (GetSpiralRing(49) == 3);
print (GetSpiralRing(65) == 4);
print (GetSpiralRing(85) == 5);

print (GetDifferenceFromBottomRightRingNum( 0, 1) == 0);
print (GetDifferenceFromBottomRightRingNum(1, 9) == 0);
print (GetDifferenceFromBottomRightRingNum(2, 25) == 0);
print (GetDifferenceFromBottomRightRingNum(3, 49) == 0);
print (GetDifferenceFromBottomRightRingNum(4, 81) == 0);

print (GetDifferenceFromBottomRightRingNum(4, 91) == 10);
print (GetDifferenceFromBottomRightRingNum(1, 18) == 9);
print (GetDifferenceFromBottomRightRingNum(2, 32) == 7);
print (GetDifferenceFromBottomRightRingNum(3, 55) == 6);
print (GetDifferenceFromBottomRightRingNum(4, 89) == 8);

print(GetShortestPath(1)==0);
print(GetShortestPath(12)==3);
print(GetShortestPath(23)==2);
print(GetShortestPath(1024)==31);"""
    
#print(GetShortestPath(368078));
#print(GetFirstNumberOfSumSpiralGreaterThanNum(368078));