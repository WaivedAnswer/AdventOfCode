def RemoveCharacterCancellations(input):
    index = input.find('!');
    while (index != -1):
        input = input[:index] + input[index+2:];
        index = input.find('!');
    return input;
    
def RemoveGarbage(input):
    startIndex = input.find('<');
    endIndex = input.find('>');
    garbageCount = 0;
    while (startIndex != -1):
        garbageChars = input[startIndex + 1: endIndex];
        garbageCount += len(garbageChars);
        input = input[:startIndex] + input[endIndex + 1:];
        startIndex = input.find('<');
        endIndex = input.find('>');
    print ("GarbageCount was : " + str(garbageCount));
    return input;

def GetCleanInput(input):
    cancelled = RemoveCharacterCancellations(input);
    return RemoveGarbage(cancelled);
    
def ScoreGroups(input):
    score = 0;
    charStack = [];
    for character in input:
        if(character == '{'):
            charStack.append('{');
            score += len(charStack);
        elif(character == '}'):
            charStack.pop();  
    return score;
    
def GetInputScore(input):
    groups = GetCleanInput(input)
    return ScoreGroups(groups);
    
def PrintInputScoreFromFile(filename):
    inputFile = open(filename);
    for line in inputFile.readlines():
        score = GetInputScore(line.rstrip());
        print(score);
        
def CountGroups(input):
    return input.count('{');
    
        
        
def PrintGroupCountFromFile(filename):
    inputFile = open(filename);
    for line in inputFile.readlines():
        groups = GetCleanInput(line.rstrip());
        print (CountGroups(groups));
        
#PrintGroupCountFromFile("testInputGrouping.txt");
#PrintInputScoreFromFile("testInputScoring.txt");

PrintInputScoreFromFile("input.txt");
        
