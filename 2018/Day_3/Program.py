import Common

def part1(input):
    twoCount = 0
    claims = []
    claimMap = []
    for i in range(1000):
        claimMap.append([]);
        for j in range(1000):
            claimMap[i].append(0)
    for line in input:
        values = line.split();
        cid = values[0]
        topLeft = values[2]
        topLeftx = int(topLeft.split(",")[0])
        topLefty = int(topLeft.split(",")[1].strip(":"))
        size = values[3]
        sizex = int(size.split("x")[0])
        sizey = int(size.split("x")[1])
        claims.append([cid, topLeftx,topLefty,sizex,sizey])
        for i in range(sizex):
            for j in range(sizey):
                claimMap[topLeftx + i][topLefty + j] = claimMap[topLeftx + i][topLefty + j] + 1
    for i in range(len(claimMap)):
        for j in range(len(claimMap[i])):
            if(claimMap[i][j] > 1):
                twoCount = twoCount + 1
    for claim in claims:
        cid = claim[0]
        topLeftx = claim[1]
        topLefty = claim[2]
        sizex = claim[3]
        sizey = claim[4]
        fail = False
        for i in range(sizex):
            for j in range(sizey):
                if(claimMap[topLeftx + i][topLefty + j] != 1 ):
                    fail = True
        if(not fail):
            print(cid)
                
        #claims[id] = topLeft

    print(twoCount)
            
input = Common.inputAsLines()
#input = Common.inputAsString()

part1(input)
#part2(input)




