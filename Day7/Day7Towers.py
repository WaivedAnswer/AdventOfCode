#day7
class Tower:
    def __init__(self, name, weight, subTowers):
        self.name = name;
        self.weight = weight;
        self.subTowers = subTowers;
        
    
def ParseInformation(information):
    words = information.split();
    name = words[0];
    weight = words[1].strip("(").strip(")");
    aboves = [];
    if("->" in words):
        aboveString = "".join(words[3:]);
        aboves = aboveString.strip().split(",");
    return (name, weight, aboves);
    
def GetCurrentLevelKey(keyLookups, currentLevelKeys):
    for key in keyLookups:
        if(key in currentLevelKeys):
            return key;
    print key, keyLookups, currentLevelKeys
    print("Something went wrong.");
    return None;
    
def GetNodeParent(name, towersKeyLookups, towers):
    nextKey = GetCurrentLevelKey(towersKeyLookups[name], towers.keys());
    currentTower = towers[nextKey];
    oldTower = None;
    #traverse tree
    while(True):
        nextKey = GetCurrentLevelKey(towersKeyLookups[name], currentTower.subTowers.keys());
        nextTower = currentTower.subTowers[nextKey];
        if(nextTower.name == name):
            break;
        currentTower = nextTower;
    
    return currentTower;
    
def AppendLookupNameToAllChildren(tower, towersKeyLookups, name):
    for subtower in tower.subTowers:
        print subtower;
        AppendLookupNameToAllChildren(subtower, towersKeyLookups, name);
        if(name not in towersKeyLookups[subTower.name]):
            towersKeyLookups[subTower.name].append(name);
    
def GetBottomTower(input):
    towers = {};
    towersKeyLookups = {};
    
    for information in input:
        (name, weight, aboves) = ParseInformation(information);
        #create subtowers
        subTowers = {};
        for aboveName in aboves:
            # has to be on root
            if(aboveName in towers.keys()):
                aboveTower = towers.pop(aboveName, None);
                if(aboveTower != None): 
                    subTowers[aboveName] = aboveTower;
                else:
                    print ("Error");
            else:
                subTowers[aboveName] = Tower(aboveName, 0, {})
            if(aboveName not in towersKeyLookups):
                towersKeyLookups[aboveName] = [];
            print subTowers[aboveName];
            #AppendLookupNameToAllChildren(subTowers[aboveName], towersKeyLookups, tower.name);
        
                
        tower = Tower(name, weight, subTowers);

                
        #add to root      
        if(name not in towersKeyLookups):
            towers[tower.name] = tower;
            towersKeyLookups[tower.name] = [""];
        #replace default on parent
        else:
             parent = GetNodeParent(tower.name, towersKeyLookups, towers);
             print parent
             for key in towersKeyLookups[parent.name]:
                 AppendLookupNameToAllChildren(tower, towersKeyLookups, key);
             parent.subTowers[tower.name] = tower;
             
    print ("BottomTower is: " + towers.values()[0].name);
    
def GetBottomTowerFromFileInput(filename):
    inputFile = open(filename);
    testInput = inputFile.readlines();
    GetBottomTower(testInput);
             

GetBottomTowerFromFileInput("input.txt");
                    
        