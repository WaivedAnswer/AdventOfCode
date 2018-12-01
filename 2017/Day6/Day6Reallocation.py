def RedistributeBlocks(currIteration):
    maxValue = max(currIteration);
    maxIndex = currIteration.index(maxValue);
    currIteration[maxIndex] = 0;

    for i in range(1, maxValue+1):
        index = (maxIndex + i) % len(currIteration);
        currIteration[index] += 1;
    return currIteration;
        

def CycleCountReallocateMemoryBanks(banks):
    cycle = 0;
    prevIterations = []
    currIteration = banks;
    
    while(currIteration not in prevIterations):
        prevIterations.append(currIteration[:]);
        currIteration = RedistributeBlocks(currIteration);
        cycle += 1;
    cycleStart = prevIterations.index(currIteration);
    print ("Cycle length is: " + str(cycle - cycleStart));
    return cycle;

inputString = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11".split();
input = [];
for item in inputString:
    input.append(int(item));
   
#print(CycleCountReallocateMemoryBanks([0,2,7,0]));
print(CycleCountReallocateMemoryBanks(input));


    