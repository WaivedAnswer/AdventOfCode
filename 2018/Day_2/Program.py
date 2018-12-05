import Common
import string
import difflib

def part1(input):
    twoCount = 0
    threeCount = 0
    for line in input:
        for c in string.ascii_lowercase:
            if(line.count(c) == 2):
                twoCount = twoCount + 1
                break
        for c in string.ascii_lowercase:
            if(line.count(c) == 3):
                threeCount = threeCount + 1

    print(twoCount * threeCount)
    
def part2(input):
    for line1 in input:
        for line2 in input:
            charDiff = []
            for i in range(len(line1)):
                if(line1[i] != line2[i]):
                    print(line1[i],line2[i])
                    charDiff.append(line1[i])
            if(len(charDiff) == 1):
                print(line1, line2)
                return
            
input = Common.inputAsLines()
#input = Common.inputAsString()

part1(input)
part2(input)




