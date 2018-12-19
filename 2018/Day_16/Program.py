#!/usr/bin/env python3#
import Common
from collections import defaultdict

def addr(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] + registers[B]
    return registers
    
def addi(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] + B
    return registers

def mulr(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] * registers[B]
    return registers

def muli(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] * B
    return registers

def banr(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] & registers[B]
    return registers
    
def bani(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] & B
    return registers
    
def borr(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] | registers[B]
    return registers
    
def bori(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A] | B
    return registers
    
def setr(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = registers[A]
    return registers
    
def seti(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = A
    return registers

def gtir(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = int(A > registers[B])
    return registers

def gtri(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = int(registers[A] > B)
    return registers

def gtrr(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = int(registers[A] > registers[B])
    return registers
    
def eqir(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = int(A == registers[B])
    return registers
    
def eqri(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = int(registers[A] == B)
    return registers
    
def eqrr(initial, parameters):
    registers = initial[:]
    opCode,A,B,C = parameters
    registers[C] = int(registers[A] == registers[B])
    return registers
    
operations = [addr, 
                addi, 
                mulr, 
                muli, 
                banr, 
                bani, 
                borr, 
                bori, 
                setr, 
                seti, 
                gtir, 
                gtri, 
                gtrr,
                eqir,
                eqri,
                eqrr]
                



def possibleOperations(sample):
    results = set()
    for operation in operations:
        if( sample.after == operation(sample.before, sample.parameters)):
            results.add(operation.__name__)
    
    return results
            
def getOperationCount(samples):
    return len([ sample for sample in samples if len(possibleOperations(sample)) >= 3])
                

class Sample:
    def __init__(self):
        self.before = None
        self.after = None
        self.parameters = None
        

    
def part1(input):
    samples = []
    currentSample = None
    for i,line in enumerate(input):
        #sampleCount = int(i / 4)
        if i % 4 == 0:
            currentSample = Sample()
            currentSample.before = Common.numbers(line)
        elif i % 4 == 1:
            currentSample.parameters = Common.numbers(line)
        elif i % 4 == 2:
            currentSample.after = Common.numbers(line)
            samples.append(currentSample)
            currentSample = None
          
    return getOperationCount(samples)

def getOpCodes(samples):
    possibleOpCodes = defaultdict(set)
    for sample in samples:
        possibles = possibleOperations(sample)
        if(len(possibleOpCodes[sample.parameters[0]]) == 0 ):
            possibleOpCodes[sample.parameters[0]] = possibles
        else:
            possibleOpCodes[sample.parameters[0]].intersection(possibles)
    print(possibleOpCodes)
    opCodes = { key:values.pop() for key,values in possibleOpCodes.items() if len(values) == 1 }
    print(opCodes)
    while len(opCodes) != len(possibleOpCodes):
        for opCode in possibleOpCodes:
            if(opCode in opCodes or len(possibleOpCodes[opCode]) < 1):
                continue
            possibles = [code for code in possibleOpCodes[opCode] if code not in opCodes.values() ]
            print(possibles)
            if(len(possibles) == 1):
                opCodes[opCode] = possibles[0]
    return opCodes
        

def part2(input):
    samples = []
    currentSample = None
    for i,line in enumerate(input):
        #sampleCount = int(i / 4)
        if i % 4 == 0:
            currentSample = Sample()
            currentSample.before = Common.numbers(line)
        elif i % 4 == 1:
            currentSample.parameters = Common.numbers(line)
        elif i % 4 == 2:
            currentSample.after = Common.numbers(line)
            samples.append(currentSample)
            currentSample = None
            
    opCodes = getOpCodes(samples)
    
    input2 = Common.fileAsLines("input2.txt")
    registers = [0,0,0,0]
    for line in input2:
        parameters = Common.numbers(line)
        operation = globals()[opCodes[parameters[0]]]
        registers = operation(registers, parameters)
        print(registers)
    
    return registers[0]
            
input = Common.inputAsLines()
#input = Common.inputAsString()

print(part1(input))
print(part2(input))
    
#print(part2(input))




