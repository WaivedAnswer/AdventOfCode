import Common
import numpy as np

def get_single_value(value, instructions):
	try:
		return int(value)
	except ValueError:
		eval = get_value(value, instructions)
		instructions[value] = str(eval)
		return eval

def get_double_value(param0, param1, instructions):
	if(param0 != "NOT"):
		raise Exception("Unsupported operations")
	value = get_single_value(param1, instructions)
	return ~value
	
def get_triple_value(param0, param1, param2, instructions):
	value1 = get_single_value(param0, instructions)
	value2 = get_single_value(param2, instructions)
	if( param1 == "AND"):
		return value1 & value2
	elif( param1 == "OR"):
		return value1 | value2
	elif( param1 == "LSHIFT"):
		return value1 << value2		
	elif( param1 == "RSHIFT"):
		return value1 >> value2
		
	raise Exception("Unsupported operations")
		
		
def evaluate(equation, instructions):
	params = equation.split()
	if(len(params) == 1):
		return get_single_value(params[0], instructions)
	elif(len(params) == 2):
		return get_double_value(params[0], params[1], instructions)
	elif(len(params) == 3):
		return get_triple_value(params[0], params[1], params[2], instructions)
	raise Exception("Unsupported operations")


def get_value(key, instructions):
	equation = instructions[key]
	return evaluate(equation, instructions)

def getValueOfAInCircuit(input):
	instructions = {}
	for line in input:
		values = line.split(" -> ")
		instructions[values[1]] = values[0]
	return get_value("a", instructions)
	
def getValueOfAInCircuit2(input):
	instructions = {"b": "956"}
	for line in input:
		values = line.split(" -> ")
		if(values[1] == "b"):
			continue
		instructions[values[1]] = values[0]
	return get_value("a", instructions)
	
assert(getValueOfAInCircuit(["123 -> a"]) == 123)
assert(getValueOfAInCircuit(["123 AND 456 -> a"]) == 72)

input = Common.inputAsLines()

#print(getValueOfAInCircuit(input))
print(getValueOfAInCircuit2(input))