def CalculateJumpStepsFromList(input):
    currentIndex = 0;
    steps = 0;
    while(len(input) > currentIndex >= 0 ):
        nextIndex = currentIndex + input[currentIndex];
        input[currentIndex] += 1;
        steps+=1;
        currentIndex = nextIndex;
    return steps;
    
def CalculateJumpStepsFromFilename(filename):
    inputfile = open(filename);
    input = [];
    for line in inputfile.readlines():
        num = int(line.strip());
        input.append(num);
    return CalculateJumpStepsFromList(input);
    

#print(CalculateJumpStepsFromFilename("testInput.txt"));
print(CalculateJumpStepsFromFilename("input.txt"));