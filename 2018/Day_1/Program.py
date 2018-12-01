import Common

def part1(input):
    sum = 0
    for line in input:
        if(line[0] == "+"):
            sum += int(line[1:])
        else:
            sum -= int(line[1:])
    print(sum)
    
def part2(input):
    differences = []
    for line in input:
        if(line[0] == "+"):
            differences.append(int(line[1:]))
        else:
            differences.append(-int(line[1:]))
        
    sum = 0
    prevValues = {}
    prevValues[sum] = True
    hasRepeat = False
    
    while not hasRepeat:
        for difference in differences:
            sum += difference
            if(sum in prevValues):
                hasRepeat = True
                break
            prevValues[sum]= True
    print(sum)
            
input = Common.inputAsLines()


part1(input)
part2(input)




