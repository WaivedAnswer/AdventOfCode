import Common


def get_corner_values(corner):
	x1,y1 = corner.split(",")
	return (int(x1), int(y1))
	
def parseCorners(input, index1, index2):
	values = input.split()
	corner1 = values[index1]
	x1,y1 = get_corner_values(corner1)
	corner2 = values[index2]
	x2,y2 = get_corner_values(corner2)
	return [x1,y1,x2,y2]
	
def applyOpToGrid(grid, op, x1, y1, x2, y2):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			grid[i][j] = op(grid[i][j])

def turn_on(input, grid, op):
	x1,y1,x2,y2 = parseCorners(input, 2, 4)
	applyOpToGrid(grid, op, x1,y1,x2,y2)
	return

def toggle(input, grid, op):
	x1,y1,x2,y2 = parseCorners(input, 1, 3)
	applyOpToGrid(grid, op, x1,y1,x2,y2)
	return

def turn_off(input, grid, op):
	x1,y1,x2,y2 = parseCorners(input, 2, 4)
	applyOpToGrid(grid,op, x1,y1,x2,y2)
	return
	
def count_grid(grid, op):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
				count = op(count, grid[i][j])
	return count

def init_grid(value, size):
	return [[value for _ in range(size) ] for _ in range(size)]
	
def light_grid(input, size):
	grid = init_grid(False, size)
	for line in input:
		if(line.startswith("turn on")):
			turn_on(line, grid, lambda a : True)
		elif(line.startswith("toggle")):
			toggle(line, grid, lambda a : not a)
		elif(line.startswith("turn off")):
			turn_off(line, grid, lambda a: False)
		else:
			continue
	return count_grid(grid, lambda a, b: a + 1 if b == True else a )
	
def light_grid2(input, size):
	grid = init_grid(0, size)
	for line in input:
		if(line.startswith("turn on")):
			turn_on(line, grid, lambda a: a + 1)
		elif(line.startswith("toggle")):
			toggle(line, grid, lambda a: a + 2)
		elif(line.startswith("turn off")):
			turn_off(line, grid, lambda a: a - 1 if a > 0 else 0 )
		else:
			continue
	return count_grid(grid, lambda a, b: a + b)
	


input = Common.inputFromLines()

#assert(light_grid(["turn on 0,0 through 999,999"], 1000) == 1000000)
#assert(light_grid(["toggle 0,0 through 999,0"], 1000) == 1000)
#assert(light_grid(["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"], 1000) == 1000000 - 4)
#print("Tests Pass")

print( light_grid(input, 1000))
print( light_grid2(input, 1000))