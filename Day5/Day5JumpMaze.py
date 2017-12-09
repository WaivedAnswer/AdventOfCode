def GetNewJumpNum(prevValue):
    if(prevValue >= 3):
        return prevValue - 1;
    return prevValue + 1;
    
def CalculateJumpStepsFromList(input, useModJumps):
    currentIndex = 0;
    steps = 0;
    while(len(input) > currentIndex >= 0 ):
        nextIndex = currentIndex + input[currentIndex];
        if(useModJumps):
            input[currentIndex] = GetNewJumpNum(input[currentIndex]);
        else:
            input[currentIndex] += 1;
        steps+=1;
        currentIndex = nextIndex;
    return steps;
    
def CalculateJumpStepsFromFilename(filename, useModJumps):
    inputfile = open(filename);
    input = [];
    for line in inputfile.readlines():
        num = int(line.strip());
        input.append(num);
    return CalculateJumpStepsFromList(input, useModJumps);
    

#print(CalculateJumpStepsFromFilename("testInput.txt", True));
print(CalculateJumpStepsFromFilename("input.txt", True));