def parseInstruction(input):
    words = input.split()
    targetRegister = words[0];
    difference = 0;
    if(words[1] == "inc"):
        difference = int(words[2]);
    elif(words[1] == "dec"):
        difference = -int(words[2]);
    
    condition = words[4:]
    
    return (targetRegister, difference, condition);

def GetPythonOperatorString(input):
    input = "".join(input);#.replace("!=", " not == ")
    return input;
    
def EvaluateCondition(condition, registers):
    if(condition[0] not in registers):
        registers[condition[0]] = 0.0;
    registerVal = registers[condition[0]];
    otherVal = int(condition[-1])
    
    return eval(str(registerVal) + GetPythonOperatorString(condition[1:-1]) + str(otherVal));

def GetLargestRegisterAfterInstructions(input):
    registers = {};
    largestValEver = 0;
    for line in input:
        (targetRegister, difference, condition) = parseInstruction(line.rstrip())
        if(EvaluateCondition(condition, registers)):
            if(targetRegister not in registers):
                registers[targetRegister] = 0;
            registers[targetRegister] += difference;
            if(registers[targetRegister] > largestValEver):
                largestValEver = registers[targetRegister];
                
    return largestValEver, max(registers.values())
    
    
def GetLargestRegisterAfterInstructionsFromFile(filename):
    inputFile = open(filename);
    input = inputFile.readlines();
    return GetLargestRegisterAfterInstructions(input);
    
print (GetLargestRegisterAfterInstructionsFromFile("input.txt"));