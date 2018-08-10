import Common
def deliverPresent(x, y, map):
	delivered = False
	if( not( x in map and y in map[x])):
		delivered = True
		if(not x in map):
			map[x] = {}
		map[x][y] = True
	return delivered
	
def move(c):
	diff = [0,0]
	if(c == "^"):
		diff[1] += 1
	elif(c == "v"):
		diff[1] -= 1
	elif(c == ">"):
		diff[0] += 1
	elif(c == "<"):
		diff[0] -= 1
	return diff

def parseDirections(input):
	map = {}
	x = 0
	y = 0
	rx = 0
	ry = 0
	presents = 0
	
	if( deliverPresent(x,y,map) ):
		presents += 1
	if( deliverPresent(rx,ry,map) ):
		presents += 1
	moveRobo = False
	for c in input:
		diff = move(c)
		if(not moveRobo):
			x += diff[0]
			y += diff[1]
			if( deliverPresent(x,y,map) ):
				presents += 1
		else:
			rx += diff[0]
			ry += diff[1]
			if( deliverPresent(rx,ry,map) ):
				presents += 1
		moveRobo = not moveRobo
	print(presents)
			


input = Common.inputAsString()
parseDirections(input)