def parseInput(filename):
	file = open(filename)
	return file.readlines()
	
def getDimensions(input):
	dimensions = []
	for instruction in instructions:
		dim = instruction.split("x")
		dimensions.append([int(dim[0]), int(dim[1]), int(dim[2])])
	return dimensions
	
def getTotalSurfaceArea(dimensions):
	total = 0
	for dim in dimensions:
		a1 = dim[0]*dim[1]
		a2 = dim[1]*dim[2]
		a3 = dim[2] * dim[0]
		total += 2* sum([a1, a2, a3])
		total += min([a1, a2, a3])
	print(total)
	
def getTotalRibbon(dimensions):
	total = 0
	for dim in dimensions:
		x = dim[0]
		y = dim[1]
		z = dim[2]
		
		vol = x * y * z
		maxdim = max(dim)
		minDims = dim
		minDims.remove(maxdim)
		
		total += 2 * sum(minDims)
		total += vol
	print(total)
	
instructions = parseInput("input.txt")
dimensions = getDimensions(instructions)
#getTotalSurfaceArea(dimensions)
#getTotalSurfaceArea([[2, 3, 4]])
#getTotalSurfaceArea([[1, 1, 10]])

getTotalRibbon(dimensions)