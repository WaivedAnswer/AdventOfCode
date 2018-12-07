#!/usr/bin/env python#
import Common
import re
from collections import defaultdict
from collections import deque

def part1(input):
    steps = defaultdict(lambda: set())
    totalSteps = set()
    for line in input:
        caps = re.sub('[^A-Z]', " ", line).split()
        init = caps[1]
        follow = caps[2]
        steps[follow].update(init)
        totalSteps.update(init, follow)
        
    
    finished = []
    while(len(finished) != len(totalSteps)):
        ready = []
        for step in totalSteps:
            if(step in finished):
                continue
            if(step not in steps or steps[step].issubset(finished)):
                ready.append(step)
        if(ready):
            finished.append(min(ready))
        
    return "".join(finished)
          
def getCharTime(c):
    return 60 + ord(c) - ord('A') + 1
  
def part2(input):
    steps = defaultdict(lambda: set())
    totalSteps = set()
    for line in input:
        caps = re.sub('[^A-Z]', " ", line).split()
        init = caps[1]
        follow = caps[2]
        steps[follow].update(init)
        totalSteps.update(init, follow)
        
    
    finished = []
    maxWorkers = 5
    worker = []
    time = 0
    while(len(finished) != len(totalSteps)):
        for i in range(len(worker)):
            worker[i] = (worker[i][0], worker[i][1] - 1)
            if(worker[i][1] <= 0):
                finished.append(worker[i][0])
        worker = [item for item in worker if item[0] not in finished]
        ready = []
        for step in totalSteps:
            if(step in finished or step in [item[0] for item in worker]):
                continue
            if(step not in steps or steps[step].issubset(finished)):
                ready.append(step)
        for nxt in sorted(ready):
            if(len(worker) >= maxWorkers):
                break
            worker.append((nxt, getCharTime(nxt)))
        
        print(time, finished, worker)
        time += 1
        
        
    return time - 1
    

            
input = Common.inputAsLines()
#input = Common.inputAsString()
print(getCharTime('A'))
print(getCharTime('B'))
#print(part1(input))
print(part2(input))




