#!/usr/bin/env python3#
import Common
from collections import defaultdict

def getManhattanDist(star1, star2):
    return sum(abs(a - b) for a,b in zip(star1,star2))
    
def getGrouped(match, matches, group):
    if(match in group):
        return
    group.add(match)
    newMatches = matches[match]
    for newMatch in newMatches:
        getGrouped(newMatch, matches, group)
    
def getGroups(matches):
    groups = []
    matched = {}
    for match in matches:
        if match in matched:
            continue
        group = set()
        getGrouped(match, matches, group)
        groups.append(group)
        for num in group:
            matched[num] = True
            
    return groups
    
def part1(input):
    stars = defaultdict(tuple)
    starNum = 0
    for line in input:
        numbers = Common.numbers(line)
        stars[starNum] = tuple(numbers)
        starNum += 1
    
    constellations = []
    matches = defaultdict(set)
    for starNum1, star1 in stars.items():
        for starNum2, star2 in stars.items():
            if getManhattanDist(star1, star2) <= 3:
                matches[starNum1].add(starNum2)
                matches[starNum2].add(starNum1)
    
    groups = getGroups(matches)
        
    return len(groups)
            
input = Common.inputAsLines()

print(part1(input)) #bounds 306-616

#print(part2(input))




