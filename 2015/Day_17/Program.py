import itertools
import Common

a = [20,15,10,5,5]

def findCombinationsOfContainers(total, containers):
	coms = []
	for i in range(1,len(containers)+1):
		coms.extend([  c for c in itertools.combinations(containers,i) if sum(c) == total ])
	return len(coms)
	
def findMinCombinationsOfContainers(total, containers):
	for i in range(1,len(containers)+1):
		coms = [  c for c in itertools.combinations(containers,i) if sum(c) == total ]
		if( not len(coms) == 0):
			return len(coms)
	return 0
	
assert( findCombinationsOfContainers(25, a) == 4)

input = Common.inputAsNums()
print( findCombinationsOfContainers(150, input))
print( findMinCombinationsOfContainers(150, input))