#day16
import string

def Spin(programs, spinCount):
    for i in range(spinCount):
        programs.insert(0, programs.pop())
    
def Exchange(programs, posA, posB):
    temp = programs[posA]
    programs[posA] = programs[posB]
    programs[posB] = temp
    
def Partner(programs, A, B):
    indexA = programs.index(A)
    indexB = programs.index(B)
    if(indexA == -1 or indexB == -1):
        print "Error!!"
        
    Exchange(programs, indexA, indexB)

    
def Day16(input, danceCount):
    programCount = 16;
    programs = [];
    for i in range(programCount):
        programs.append(string.ascii_lowercase[i])
    
    originalprograms = programs[:];
    count = 0;
    seen = [];
    cycleLength = 1;
    seen.append(programs[:])
    
    while True:
        for line in input:
            if(line[0] == 's'):
                Spin(programs, int(line[1:]))
            elif(line[0] == 'x'):
                vals = line[1:].split('/')
                Exchange(programs, int(vals[0]), int(vals[1]))
            elif(line[0] == 'p'):
                vals = line[1:].split('/')
                Partner(programs, vals[0], vals[1])
        count +=1
        seen.append(programs[:]);
        if("".join(programs) == "".join(originalprograms)):
            cycleLength = count
            break;

    seenCount = (danceCount) % cycleLength
    #print seen
    print "".join(seen[seenCount])
    
    
def Day16File(filename, danceCount):
    file = open(filename)
    text = "".join("".join(line.split()) for line in file)
    #print text
    Day16(text.split(','), danceCount)
    
            
#Day16(["pe/b"]);
#Day16File("testInput.txt")
#Day16(["s15"])
Day16File("input.txt", 1)
Day16File("input.txt", 1000000000)
        