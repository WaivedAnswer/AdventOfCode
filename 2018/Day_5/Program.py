import Common
import collections
import re
import string

def collapse(cs):
    prevC = None
    newChars = []
    for c in cs:
        if(prevC and c.lower() == prevC.lower() and not c.islower() == prevC.islower()):
            newChars.pop()
            prevC = None
        else:
            newChars.append(c)
            prevC = c
    return newChars
    
def collapseList(cs):
    while(True):
        newcs = collapse(cs)
        if(len(cs) == len(newcs)):
            return newcs
        cs = newcs
    return None
    
def part1(input):
    cs = [c for c in input]
    return len(collapseList(cs))
    
def part2(input):
    newcs = collapseList(input)
    lengths = {}
    for c in string.ascii_lowercase:
        removedChars = re.sub(c, '', ''.join(newcs), flags=re.IGNORECASE)
        lengths[c] = len(collapseList(removedChars))
    return min(lengths.items(), key = lambda x: x[1])
        
            
input = Common.inputAsString()
print(part1(input))
print(part2(input))




