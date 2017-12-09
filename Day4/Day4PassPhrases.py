from sets import Set

def GetSortedWord(word):
    return ''.join(sorted(word));
        
def CheckPassPhraseValidity(input, isAnagramCheck):
    previousWords= {};
    words = input.split();
    for word in words:
        if(isAnagramCheck):
            word = GetSortedWord(word);
        if word in previousWords:
            return False;
        else:
            previousWords[word] = True;
    return True;
    
def CheckPhraseValidityCount(filename, isAnagramCheck):
    inputfile = open(filename);
    text = inputfile.readlines();
    validPhrases = 0;
    
    for line in text:
        if(CheckPassPhraseValidity(line, isAnagramCheck)):
            validPhrases = validPhrases + 1;
        
            
    return validPhrases;
        

#print(CheckPassPhraseValidity("aa bb cc dd ee") == True);
#print(CheckPassPhraseValidity("aa bb cc dd aa") == False);
#print(CheckPassPhraseValidity("aa bb cc dd aaa") == True);


print(CheckPhraseValidityCount("Day4TextInput.txt", True));
#print(CheckPhraseValidityCount("test.txt"));
