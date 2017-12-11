#Day12

def Day12(input):
    steps = input.split(",");
    print "Test"
    
    
def Day12File(filename):
    inputFile = open(filename);
    text = inputFile.readlines();
    input = "".join(text).strip();
    Day12(input);
    
Day12File("testInput.txt");
Day12File("input.txt")