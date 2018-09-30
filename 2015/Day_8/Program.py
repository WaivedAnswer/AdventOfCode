import Common
import re

def getRawCount(value):
    return len(value)

def getEncodedCount(value):
    stripped = value
    basicAdd = [r"\\", r"\""]
    addCount = 0
    for ex in basicAdd:
        addCount = addCount + stripped.count(ex) * 4
        stripped = stripped.replace(ex,"")
        
    hexExpression = r"\\x[0-9A-Fa-f][0-9A-Fa-f]"
    
    matches = re.findall(hexExpression, stripped)
    if(matches):
        addCount = addCount + len(matches) * 5
        stripped = re.sub(hexExpression, "", stripped)
        
    return len(stripped) + addCount + 4

    
def getCount(value):
    if(len(value)==0 or value == "\"\""):
        return 0
    stripped = value
    basicRemove = [r"\\", r"\""]
    removeCount = 0
    for ex in basicRemove:
        removeCount = removeCount + stripped.count(ex)
        stripped = stripped.replace(ex,"")
        print(stripped, removeCount)
        
    hexExpression = r"\\x[0-9A-Fa-f][0-9A-Fa-f]"
    print(removeCount)
    matches = re.findall(hexExpression, stripped)
    if(matches):
        removeCount = removeCount + len(matches)
        stripped = re.sub(hexExpression, "", stripped)
    print(stripped, len(stripped), removeCount)
    return len(stripped) + removeCount - 2
    
def get_total_count_difference(input):
    count = 0
    for line in input:
        rawCount = getRawCount(line)
        memoryCount = getCount(line)
        print(line, rawCount, memoryCount)
        count = count + rawCount - memoryCount
    return count
    
def get_total_count_difference_2(input):
    count = 0
    for line in input:
        rawCount = getRawCount(line)
        encodedCount = getEncodedCount(line)
        print(line, rawCount, encodedCount)
        count = count + encodedCount - rawCount
    return count
    

testInput1 = Common.fileAsLines("Test1.txt")
assert(get_total_count_difference(testInput1) == 2)

testInput2 = Common.fileAsLines("Test2.txt")
assert(get_total_count_difference(testInput2) == 10)#42 - 32

testInput3 = Common.fileAsLines("Test3.txt")
assert(get_total_count_difference(testInput3) == 2)

testInput5 = Common.fileAsLines("Test5.txt")
assert(get_total_count_difference(testInput5) == 5)

testInput4 = Common.fileAsLines("Test4.txt")
assert(get_total_count_difference(testInput4) == 10)#28 - 18

print("Tests pass.")

input = Common.inputAsLines()
print(get_total_count_difference(input))

testInput1 = Common.fileAsLines("Test1.txt")
assert(get_total_count_difference_2(testInput1) == 4)

testInput2 = Common.fileAsLines("Test2.txt")
assert(get_total_count_difference_2(testInput2) == 15)

testInput3 = Common.fileAsLines("Test3.txt")
assert(get_total_count_difference_2(testInput3) == 4)

testInput5 = Common.fileAsLines("Test5.txt")
assert(get_total_count_difference_2(testInput5) == 5)

testInput4 = Common.fileAsLines("Test4.txt")
assert(get_total_count_difference_2(testInput4) == 10)#28 - 18

print(get_total_count_difference_2(input))

