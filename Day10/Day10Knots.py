#day10
from operator import ior;
import numpy as np;
def ReplaceItems(oldList, subList, startIndex, endIndex, doesWrap):
    
    if(not doesWrap):
        count = 0;
        for index in range(startIndex, endIndex):
            oldList[index] = subList[count];
            count += 1;
    else:
        count = 0;
        for index in range(startIndex, len(oldList)):
            oldList[index] = subList[count];
            count += 1;
        for index in range(0, endIndex):
            oldList[index] = subList[count];
            count += 1;
    
    return oldList;
        
def GetNextPos(currentPos, length, skipSize, listLength):
    return (currentPos + length + skipSize) % listLength;

def KnotHash(input, listSize, rounds):
    currentPos = 0;
    numList = range(listSize);
    skipSize = 0;
    for round in range(rounds):
        for length in input:
            doesWrap = False;
            start = currentPos;
            end = (currentPos + length);
            listLength = len(numList);
            if(end > listLength):
                doesWrap = True;
                end = end % listLength;
            
            if(not doesWrap):
                subList = numList[start:end];
            else:
                subList = numList[start:] + numList[:end];
            
            subList.reverse();

            numList = ReplaceItems(numList, subList, start, end, doesWrap);

            currentPos = GetNextPos(currentPos, length, skipSize, len(numList));

            skipSize += 1;
            
    return numList;
        
        
        
def CalcKnotHash(input, listSize):
    finalList = KnotHash(input, listSize, 1);
    print("First two multiplied gives: " + str(finalList[0] * finalList[1]));
    
def GetXor(input):
    arr = np.array(input);
    return np.bitwise_xor.reduce(arr);
    
def GetDenseHash(sparseHash):
    denseHash = [];
    for i in range(len(sparseHash)/16):
        dense = GetXor(sparseHash[i*16:(i+1)*16]);
        denseHash.append(dense);
    return denseHash;
    
def GetHexString(input):
    hexString = "";
    for item in input:
        hexString = hexString + format(item, "02x");
    return hexString;
    
def DenseHash(input):
    
    input = input.strip();
    ascii = [];
    for character in input:
        ascii.append(ord(character));
        
    additionalLengths = [17,31,73,47,23];
    ascii.extend(additionalLengths);
    
    sparseHash = KnotHash(ascii, 256, 64);
    denseHash = GetDenseHash(sparseHash)
    hexString = GetHexString(denseHash);
    print len(hexString), hexString
    
#CalcKnotHash([106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118], 256);
DenseHash("106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118");
DenseHash("");
#DenseHash("AoC 2017");

