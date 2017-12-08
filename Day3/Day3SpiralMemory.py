# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:56:51 2017

@author: WFN53616
"""
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
    return num - CalcBottomRightRingNum(ringNum);

#measured from 1
def GetCoordinates(ringNum, diff):
    if(ringNum == 0):
        if(diff == 0):
            return (0,0);
        else:
            raise Exception("incorrect inputs");
    maxDiff = CalcBottomRightRingNum(ringNum) - CalcBottomRightRingNum(ringNum - 1);
    if(maxDiff > diff):
        raise Exception("You cannot be on this ring")
    coordinates = (ringNum, ringNum);
    sideSteps = ringNum * 2;
    for i in range(diff):
        #left
        if(i/sideSteps == 0):
            coordinates[0]-=1;
        # up
        elif(i/sideSteps == 1):
            coordinates[1]-=1;
        #right
        elif(i/sideSteps == 2):
            coordinates[0]+=1;
        #down
        elif(i/sideSteps == 3):
            coordinates[1]+=1;
    return coordinates
        
        
    

def GetSpiralCoordinates(num):
    ringNum = GetRingNum(num);
    diff = GetDifferenceFromBottomRightRingNum(ringNum, num);
    return GetCoordinates(ringNum, diff);


print (GetDifferenceFromBottomRightRingNum( 0, 1) == 0);
print (GetDifferenceFromBottomRightRingNum(1, 9) == 0);
print (GetDifferenceFromBottomRightRingNum(2, 25) == 0);
print (GetDifferenceFromBottomRightRingNum(3, 49) == 0);
print (GetDifferenceFromBottomRightRingNum(4, 81) == 0);    

"""print (CalcBottomRightRingNum(0) == 1);
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
print (GetDifferenceFromBottomRightRingNum(4, 89) == 8);"""