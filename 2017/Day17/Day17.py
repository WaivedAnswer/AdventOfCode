#day17

def Day17(stepCount):
    sBuffer = [0]
    spinCount = 2017
    currPos = 0;
    for i in range(1,spinCount + 1):
        stepPos = (currPos + stepCount) % len(sBuffer) + 1
        sBuffer.insert(stepPos, i)
        currPos = stepPos
    print sBuffer[currPos + 1];
    
def Day17P2(stepCount):
    valNextToZero = -1
    sBufferCount = 1
    spinCount = 50000000
    currPos = 0;
    for i in range(1,spinCount + 1):
        stepPos = (currPos + stepCount) % sBufferCount + 1
        if(stepPos == 1):
            valNextToZero = i
        sBufferCount += 1
        currPos = stepPos
        
    print valNextToZero;
    
    
#Day17(371)
Day17P2(371)
    