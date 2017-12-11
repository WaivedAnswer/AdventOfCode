#day7
class Tower:
    def __init__(self, name, weight, aboves):
        self.name = name;
        self.weight = weight;
        self.aboves = aboves;
        
    
def ParseInformation(information):
    words = information.split();
    name = words[0];
    weight = int(words[1].strip("(").strip(")"));
    aboves = [];
    if("->" in words):
        aboveString = "".join(words[3:]);
        aboves = aboveString.strip().split(",");
    return (name, weight, aboves);
    
def GetTowerWeights(towers, currKey):
    
    currTower = towers[currKey];
    weight = currTower.weight;
    if(len(currTower.aboves) == 0):
        return weight;
        
    weights = [];
    keys = [];
    setWeights = [];
    differentWeight = (None, None);
    
    for above in currTower.aboves:
        subWeight = GetTowerWeights(towers, above);
        keys.append(above);
        weights.append(subWeight);
        setWeights = set(weights);
        
    if(len(setWeights) > 1): 
        print setWeights, weights
        requiredWeight = [w for w in setWeights if weights.count(w) > 1][0];
        diffWeight = [w for w in setWeights if weights.count(w) == 1][0];
        baseWeightIndex = weights.index(diffWeight);
        baseWeight = towers[keys[baseWeightIndex]].weight;
        print( "Different weight needs to be: " + str(requiredWeight));
        print ("Different weight needs to change to: " + str(baseWeight - (diffWeight - requiredWeight)) );
        
    weight += sum(weights);
    return weight;
    
def GetBottomTower(input):
    towers = {};
    subTowers = {};
    for information in input:
        (name, weight, aboves) = ParseInformation(information);
        tower = Tower(name,weight,aboves);
        for name in aboves:
            subTowers[name] = True;
        towers[tower.name] = tower;
    bottom = [key for key in towers.keys() if key not in subTowers.keys()];
    weight = GetTowerWeights(towers, bottom[0]);
    
    print bottom;
    print ("Total weight: " + str(weight));
    
def GetBottomTowerFromFileInput(filename):
    inputFile = open(filename);
    testInput = inputFile.readlines();
    GetBottomTower(testInput);
             

GetBottomTowerFromFileInput("input.txt");
                    
        