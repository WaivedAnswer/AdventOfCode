  
def GenerateNextA(curr):
    factor = 16807;
    return (curr * factor) % 2147483647;
def GenerateNextB(curr):
    factor = 48271
    return (curr * factor) % 2147483647;
    
def GetLast16Bits(val):
    mask = (1 << 16) - 1;
    return val & mask;
    
def CompareLast16Bits(valA, valB):
    return GetLast16Bits(valA) == GetLast16Bits(valB);
    
def Day15(first1, first2):
    valA = GenerateNextA(first1);
    valB = GenerateNextB(first2);
    iter = 40000000;
    match = 0;
    
    for i in range(iter):
        if(CompareLast16Bits(valA, valB)):
            match += 1;
        valA = GenerateNextA(valA);
        valB = GenerateNextB(valB);
        
def Day15Part2(first1, first2):
    valA = GenerateNextA(first1);
    valB = GenerateNextB(first2);
    iter = 5000000;
    match = 0;
    AValues = [];
    BValues = [];
    pairs = 0;
    while True:
        if(pairs >= iter):
            break;
        if(valA % 4 == 0):
            AValues.append(valA);
        if(valB % 8 == 0):
            BValues.append(valB);
        if(pairs < min(len(AValues), len(BValues))):
            if(CompareLast16Bits(AValues[pairs], BValues[pairs])):
                match += 1;
            pairs += 1;
            
        valA = GenerateNextA(valA);
        valB = GenerateNextB(valB);
        
        
    print match;
    
#Day15(65,8921);
#Day15(634,301);

Day15Part2(634,301);
