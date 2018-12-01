#day13
        
def CheckScannerHit(pos, scanners, delay):
    if(pos not in scanners):
        return False;
    return (pos + delay) % (2*(scanners[pos][1] - 1)) == 0;
    
        
def CheckInfractionSeverity(pos, scanners):
    if(CheckScannerHit(pos, scanners, 0)):
        possible = scanners[pos];
        return possible[1] * pos;
    return 0;

    
def Fewest(scanners, maxLayer):
    delay = 0;
    while(True):
        hit = False;
        for packetPos in range(0, maxLayer + 1):
            if(CheckScannerHit(packetPos, scanners, delay)):
                hit = True;
                break;
        if(hit == False):
            print ("Avoided if delay = " + str(delay));
            return;
        delay += 1;

def Day13(input):
    scanners = {};
    maxLayer = 0;
    
    for line in input:
        words = "".join(line.split(":")).split();
        depth = int(words[0]);
        rangeP = int(words[1]);
        if(depth > maxLayer):
            maxLayer = depth;
        scanners[depth] = (0, rangeP);
        
    severity = 0;
    for packetPos in range(maxLayer + 1):
        severity += CheckInfractionSeverity(packetPos, scanners);
    
    print severity;
    Fewest(scanners, maxLayer);
        
def Day13TestFile(filename):
    inputFile = open(filename);
    text = inputFile.readlines();
    
    Day13(text);
    
Day13TestFile("testInput.txt")
#Day13TestFile("input.txt")