#day14
import numpy as np;

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
    return hexString
    
def DecryptHash(input):
    strHex = ""
    num_of_bits = 4;
    for char in input:
        test = bin(int(char, 16))[2:].zfill(num_of_bits)
        strHex += test;
    return strHex;
    
def GetHashKey(coords, grid):
    width = len(grid[0]);
    return width*coords[0] + coords[1];
    
def GetCoords(key, grid):
    width = len(grid[0]);
    coordX = key /width;
    coordY = key % width;
    return (coordX, coordY);
    
def GetTotalRegion(coords, grid, hashTable, regionNum):
    if(grid[coords[0]][coords[1]] == False):
        return None;
    key = GetHashKey((coords[0], coords[1]), grid);
    if(key in hashTable):
        return None;
    region = []
    region.append(key);
    hashTable[key] = regionNum;

    if(coords[0] > 0):
        extra = GetTotalRegion((coords[0]-1,coords[1]), grid, hashTable, regionNum);
        if(extra != None):
            region.extend(extra);
    if(coords[0] < len(grid) - 1):
        extra = GetTotalRegion((coords[0]+1,coords[1]), grid, hashTable, regionNum);
        if(extra != None):
            region.extend(extra);
    if(coords[1] > 0):
        extra = GetTotalRegion((coords[0],coords[1]-1), grid, hashTable, regionNum);
        if(extra != None):
            region.extend(extra);
    if(coords[1] < len(grid[coords[0]]) - 1):
        extra = GetTotalRegion((coords[0], coords[1]+1), grid, hashTable, regionNum);
        if(extra != None):
            region.extend(extra);

            
    return region;
    
def CountRegions(grid):
    hashTable =  {};
    regions = [];
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == True):
                key = GetHashKey((i,j), grid);
                if(key in hashTable):
                    continue;
                newRegion = GetTotalRegion((i,j), grid, hashTable, len(regions));
                regions.append(newRegion);
                
    print ("Regions: " + str(len(regions)))
                
    
def Day14(input):
    count = 128;
    used = 0;
    grid = np.zeros((count, count))
    for i in range(count):
        key = input + "-" + str(i);
        hash = DenseHash(key);
        strVal = DecryptHash(hash);
        counter = 0;
        for char in strVal:
            if(char == "0"):
                grid[i][counter] = False;
            elif char == "1":
                used += 1;
                grid[i][counter] = True;
            counter+=1;
                
    print ("Used: " + str(used));
    CountRegions(grid)
    
        
    
#Day14("flqrgnkx")
Day14("stpzcrnm")
#Day14TestFile("input.txt")