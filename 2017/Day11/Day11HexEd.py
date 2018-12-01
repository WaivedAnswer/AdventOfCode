import numpy as np;

def GetDirection(step, coords):
    directions = {};
    
    directions["n"] = (-1,1);
    directions["s"] = (1,-1);
    
    directions["ne"] = (0, 1);
    directions["nw"] = (-1, 0);
    directions["se"] = (1, 0);
    directions["sw"] = (0, -1);
    
    """if(coords[1] % 2 == 0):
        directions["ne"] = (-1, 1);
        directions["nw"] = (-1,-1);
        directions["se"] = (0, 1);
        directions["sw"] = (0,-1);
    else:
        directions["ne"] = (0, 1);
        directions["nw"] = (0,-1);
        directions["se"] = (1, 1);
        directions["sw"] = (1,-1);"""

    
    return directions[step];

def GetNewCoords(step, childCoords):
    direction = GetDirection(step, childCoords);
    
    return [childCoords[0] + direction[0], childCoords[1] + direction[1]];
    
    
def GetShortestSteps(startCoords, childCoords):

    diffX = abs(startCoords[0] - childCoords[0]);
    diffY = abs(startCoords[1] - childCoords[1]);
    zstart = - startCoords[0] -startCoords[1];
    zchild = - childCoords[0] -childCoords[1];
    diffZ = abs(zstart - zchild);
    return max(diffX,diffY, diffZ);
    

def FewestStepsToChildHex(input):
    steps = input.split(",");
    
    startCoords = [0,0];
    childCoords = startCoords;
    maxDist = 0;
    for step in steps:
        childCoords = GetNewCoords(step, childCoords);
        maxDist = max(maxDist, GetShortestSteps(startCoords, childCoords))
        
    print ("Max Distance: " + str(maxDist));
    print ("It takes " + str(GetShortestSteps(startCoords, childCoords)) + " steps");
    
def FewestFile(filename):
    inputFile = open(filename);
    text = inputFile.readlines();
    input = "".join(text).strip();
    FewestStepsToChildHex(input);

FewestStepsToChildHex("ne,ne,ne");
FewestStepsToChildHex("ne,s,nw");
FewestStepsToChildHex("ne,ne,sw,sw");
FewestStepsToChildHex("ne,ne,s,s");
FewestStepsToChildHex("se,sw,se,sw,sw");
FewestFile("input.txt");

        
        