#Day12

def FindConnected(nodeId, nodes, connected):
    #print nodes;
    if(nodeId not in connected):
        connected.append(nodeId);
    node = nodes[nodeId];
    for connect in node:
        if connect not in connected:
            #print connect, connected;
            connected.append(connect);
            FindConnected(connect, nodes, connected);
        else:
            continue;
    
def FindGroups(ids, nodes):
    
    groups = [];
    
    while(True):
        currID = None;
        for key in ids.keys():
            if(ids[key] == False):
                currID = key;
                break;
        if(currID == None):
            break;
        connected = [];
        FindConnected(currID, nodes, connected);
        groups.append(connected);
        for connectId in connected:
            ids[connectId] = True;
        
    print ("There are groups: " + str(len(groups)));
    
def Day12(input):
    nodes = {};
    idHash = {};
    for line in input:
        line.strip();
        ids = line.strip().split("<->");
        #print ids;
        nodeId = int(ids[0].strip());
        idHash[nodeId] = False;
        reconnected = "".join(ids[1]).split(",");
        connected = [];
        for connect in reconnected:
            connected.append(int(connect.strip()));
        nodes[nodeId] = connected;
        
    test = []
    
    FindConnected(0, nodes, test);
    
    FindGroups(idHash, nodes);
    print len(test);
    
def Day12File(filename):
    inputFile = open(filename);
    text = inputFile.readlines();
    
    Day12(text);
    
def Day12TestFile(filename):
    inputFile = open(filename);
    text = inputFile.readlines();
    
    Day12(text);
    
#Day12TestFile("testInput.txt");
Day12File("input.txt")