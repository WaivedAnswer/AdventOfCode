def isDigit(word):
    try:
        int(word)
        return True
    except ValueError:
        return False
#day18
def Day18(input):
    registers = {}
    lastSound = 0
    counter = 0
    while True:
        if(counter >= len(input)):
            break;
        line = input[counter].strip()
        skip = 1

        words = line.split()
        if(words[1] not in registers):
            registers[words[1]] = 0
        if(words[0] == "snd"):
            lastSound = registers[words[1]]
        elif(words[0] == "set"):
            registers[words[1]] = int(words[2]) if isDigit(words[2]) else registers[words[2]]
        elif(words[0] == "add"):
            registers[words[1]] += int(words[2]) if isDigit(words[2]) else registers[words[2]]
        elif(words[0] == "mul"):
            registers[words[1]] *= int(words[2]) if isDigit(words[2]) else registers[words[2]]
        elif(words[0] == "mod"):
            registers[words[1]] %= int(words[2]) if isDigit(words[2]) else registers[words[2]]
            
        elif(words[0] == "rcv"):
            if(registers[words[1]] != 0):
                print (lastSound)
                break
        elif(words[0] == "jgz"):
            if(registers[words[1]] > 0): 
                skip = int(words[2])
        counter += skip;
        
def ExecuteInstruction(registers, input, lineCount, sendList, receiveList):
    sentCount = 0
    skip = 1
    if(lineCount >= len(input)):
        return False, lineCount, sentCount
    line = input[lineCount].strip()
    
    words = line.split()
    
    if(words[1] not in registers):
        registers[words[1]] = 0

    if(words[0] == "snd"):
        sendList.append(int(words[1]) if isDigit(words[1]) else registers[words[1]])
        sentCount += 1
    elif(words[0] == "set"):
        registers[words[1]] = int(words[2]) if isDigit(words[2]) else registers[words[2]]
    elif(words[0] == "add"):
        registers[words[1]] += int(words[2]) if isDigit(words[2]) else registers[words[2]]
    elif(words[0] == "mul"):
        registers[words[1]] *= int(words[2]) if isDigit(words[2]) else registers[words[2]]
    elif(words[0] == "mod"):
        registers[words[1]] %= int(words[2]) if isDigit(words[2]) else registers[words[2]]
    elif(words[0] == "rcv"):
        if(len(receiveList) == 0):
            return False, lineCount, sentCount
        registers[words[1]] = receiveList.pop(0)
    elif(words[0] == "jgz"):
        reg = int(words[1]) if isDigit(words[1]) else registers[words[1]]
        if(reg > 0): 
            skip = int(words[2]) if isDigit(words[2]) else registers[words[2]]
            
    lineCount += skip;
    return True, lineCount, sentCount

def Day18P2(input):
    registers0 = {}
    registers1 = {}
    registers0['p'] = 0
    registers1['p'] = 1
    counter0 = 0
    counter1 = 0
    Sent0 = []
    Sent1 = []
    sentCount1 = 0

    running0 = True
    running1 = True
    while (running0 or running1):
        running0, counter0, sendCount = ExecuteInstruction(registers0, input, counter0, Sent0, Sent1)
        running1, counter1, sendCount = ExecuteInstruction(registers1, input, counter1, Sent1, Sent0)
        
        sentCount1 += sendCount
        
    print (sentCount1)
        
def Day18File(filename):
    testFile = open(filename)
    text = testFile.readlines()
    #Day18(text);
    Day18P2(text);
    
#Day18File("testInput.txt") 
Day18File("input.txt")