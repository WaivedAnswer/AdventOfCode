import Common
import math

def getDistance(speed, flyduration, restduration, seconds):
	totalduration = flyduration + restduration
	cycles = math.floor(seconds / totalduration)
	extra = seconds % totalduration
	distance = cycles * flyduration * speed + min(extra * speed, flyduration * speed)
	return distance

def getReindeerDistance(line, seconds):
	words = line.split()
	name = words[0]
	speed = int(words[3])
	duration = int(words[6])
	rest = int(words[13])
	return getDistance(speed, duration, rest, seconds)
	
def getFastestReindeerDistance(input,seconds):
	maxDist = 0
	for line in input:
		dist = getReindeerDistance(line, seconds)
		if(dist > maxDist):
			maxDist = dist
	return maxDist

#can definitely speed this up
def getMostReindeerPoints(input,seconds):
	points = {}

	for i in range(1,seconds):
		maxDist = 0
		currLeaders = []
		for line in input:
			name = line.split()[0]
			if(name not in points):
				points[name] = 0
			dist = getReindeerDistance(line, i)
			if(dist > maxDist):
				currLeaders = [name]
				maxDist = dist
			elif(dist == maxDist):
				currLeaders.append(name)
		for leader in currLeaders:
			points[leader] = points[leader] + 1
		
	return max(points.values())
	
assert(getReindeerDistance("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", 1) == 14)
assert(getReindeerDistance("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", 10) == 140)
assert(getReindeerDistance("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", 11) == 140)
assert(getReindeerDistance("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", 12) == 140)
assert(getReindeerDistance("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", 1000) == 1120)
	
	

	
input = Common.inputAsLines()
print(getFastestReindeerDistance(input, 2503))
assert(getMostReindeerPoints(
["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.", 
"Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."], 1000) == 689)
print(getMostReindeerPoints(input, 2503))
