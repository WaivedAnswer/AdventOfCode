import Common
import datetime
from collections import defaultdict
import operator
from enum import Enum

class State(Enum):
	BEGIN = 0
	WAKE = 1
	SLEEP = 2

def part1(input):
	entries = {}
	for line in input:
		numbers = Common.numbers(line)
		date = datetime.datetime(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])
		gid = None
		if(len(numbers) == 6):
			gid = numbers[5]
		state = None
		if("wakes" in line):
			state = State.WAKE
		elif("falls" in line):
			state = State.SLEEP
		else:
			state = State.BEGIN
			
		entries[date] = (gid, state)
	
	prev_gid = None
	sleepTime = None
	sleepTotals = defaultdict(int)
	sleepMinutes = defaultdict(lambda: defaultdict(int))
	for date, guardState in sorted(entries.items()):
		gid = prev_gid
		if(guardState[0]):
			gid = guardState[0]
		state = guardState[1]
		if(state == State.SLEEP):
			sleepTime = date
		elif(state == State.WAKE):
			time = ((date - sleepTime).total_seconds())/60
			sleepTotals[gid] += time
			for minute in range(sleepTime.minute, date.minute):
				sleepMinutes[gid][minute] += 1
			sleepTime = None
		else:
			sleepTime = None
		prev_gid = gid
		
	max_gid = Common.maxValuePair(sleepTotals)[0]
	max_minute = Common.maxValuePair(sleepMinutes[max_gid])[0]
	print(max_gid, max_minute)
	print(max_minute * max_gid)
	
	maxGuardMinutes = [(gid, Common.maxValuePair(minutes)) for gid, minutes in sleepMinutes.items()]
	maxValues = max(maxGuardMinutes, key = lambda a:a[1][1])
	max_gid2 = maxValues[0]
	max_minute2 = maxValues[1][0]
	print(max_gid2, max_minute2)
	print(max_minute2 * max_gid2)
	


input = Common.inputAsLines()
part1(input)