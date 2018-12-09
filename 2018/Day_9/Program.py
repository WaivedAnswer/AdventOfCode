#!/usr/bin/env python#
import Common
import re
import itertools
from collections import defaultdict
from collections import deque      

def parseInput(input):
       numbers = Common.numbers(input)
       players = numbers[0]
       last = numbers[1]
       return players,last
       
       
def placeMarble(i, player, scores, marbles, currMarbleIndex):
       if(i % 23 == 0):
              removePos = (currMarbleIndex - 7) % len(marbles)
              marbles.rotate(-removePos)
              scores[player] +=  i + marbles.popleft()
              
              currMarbleIndex = 0
       else:
              insertPos = (currMarbleIndex + 2) % len(marbles)
              marbles.insert(insertPos, i)
              
              currMarbleIndex = insertPos
              
       return currMarbleIndex
       
       
def getMaxScore(players, last):
       scores = defaultdict(int)
       marbles = deque([], maxlen=last)
       marbles.insert(0, 0)
       currMarbleIndex = 0
       
       for i in range(1, last + 1):
              currPlayer = i % players
              currMarbleIndex = placeMarble(i, currPlayer, scores, marbles, currMarbleIndex)
              
       return max(scores.items(), key = lambda x: x[1])
       
       
def part1(input):
       players,last = parseInput(input)
       return getMaxScore(players, last)
   
   
def part2(input):
       players,last = parseInput(input)
       return getMaxScore(players, last * 100)
       
          
input = Common.inputAsString()
#input = Common.inputAsString()
print(part1("9 25"))
print(part1(input))
print(part2(input))




