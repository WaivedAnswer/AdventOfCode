from collections import defaultdict
import re
import networkx as nx
import copy


def get_op_code(augmented_op):
    return augmented_op % 100

def get_new_pos(old_pos, move_vector):
  return tuple(dim + move for dim, move in zip(old_pos, move_vector))


class Buffer:
    def __init__(self):
        self.buffer = []

    def post(self, val):
        self.buffer.append(val)

    def is_empty(self):
        return len(self.buffer) == 0

    def get(self):
        assert (not self.is_empty())
        return self.buffer.pop(0)


class IntProgram:
    def __init__(self, initial_registers, input_buffer, output_buffer):
        self.instructions = {
            1: self.add,
            2: self.mult,
            3: self.inp,
            4: self.out,
            5: self.jmp_true,
            6: self.jmp_false,
            7: self.less_than,
            8: self.equals,
            9: self.rel
        }
        self.registers = defaultdict(int)
        for idx, initial_value in enumerate(initial_registers):
            self.registers[idx] = initial_value
        self.relative_base = 0
        self.index = 0
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer
        self.completed = False

    def run(self):

        while True:
            op_code = get_op_code(self.registers[self.index])
            if op_code == 99:
                self.completed = True
                break
            elif op_code in self.instructions:
                instruction = self.instructions[op_code]
                old_index = self.index
                self.index = instruction(self.registers, self.index)
                if old_index == self.index:
                    break

    def get_param_mode(self, augmented_op, param_num):
        divisor = pow(10, param_num + 2)
        mod = (augmented_op % (10 * divisor))
        return int(mod / divisor)

    def get_inputs(self, registers, ip, size):
        inputs = []
        for i in range(size):
            inputs.append(registers[ip + i])
        return inputs

    def set_value(self, registers, in_address, param_mode, value):
        if param_mode == 0:
            registers[in_address] = value
        elif param_mode == 1:
            assert (0)
        elif param_mode == 2:
            registers[self.relative_base + in_address] = value
        else:
            assert 0

    def get_value(self, registers, param_value, param_mode):
        if param_mode == 0:
            return registers[param_value]
        elif param_mode == 1:
            return param_value
        elif param_mode == 2:
            return registers[self.relative_base + param_value]
        else:
            assert 0

    def get_param_modes(self, augmented_op, size):
        return [self.get_param_mode(augmented_op, num) for num in range(size - 1)]

    def add(self, registers, ip):
        size = 4
        augmented_op, noun, verb, result = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        result_value = self.get_value(registers, noun, param_modes[0]) + self.get_value(registers, verb, param_modes[1])
        self.set_value(registers, result, param_modes[2], result_value)
        return ip + size

    def mult(self, registers, ip):
        size = 4
        augmented_op, noun, verb, result = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        result_value = self.get_value(registers, noun, param_modes[0]) * self.get_value(registers, verb, param_modes[1])
        self.set_value(registers, result, param_modes[2], result_value)

        return ip + size

    def jmp_true(self, registers, ip):
        size = 3
        augmented_op, first, second = self.get_inputs(registers, ip, size)
        param_modes = param_modes = self.get_param_modes(augmented_op, size)
        if self.get_value(registers, first, param_modes[0]) != 0:
            return self.get_value(registers, second, param_modes[1])
        else:
            return ip + size

    def jmp_false(self, registers, ip):
        size = 3
        augmented_op, first, second = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        if self.get_value(registers, first, param_modes[0]) == 0:
            return self.get_value(registers, second, param_modes[1])
        else:
            return ip + size

    def less_than(self, registers, ip):
        size = 4
        augmented_op, noun, verb, result = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        result_value = self.get_value(registers, noun, param_modes[0]) < self.get_value(registers, verb, param_modes[1])
        self.set_value(registers, result, param_modes[2], result_value)
        return ip + size

    def equals(self, registers, ip):
        size = 4
        augmented_op, noun, verb, result = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        result_value = self.get_value(registers, noun, param_modes[0]) == self.get_value(registers, verb,
                                                                                         param_modes[1])
        self.set_value(registers, result, param_modes[2], result_value)
        return ip + size

    def inp(self, registers, ip):
        size = 2
        augmented_op, result = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        if self.input_buffer.is_empty():
            return ip

        in_val = self.input_buffer.get()
        self.set_value(registers, result, param_modes[0], in_val)
        return ip + size

    def out(self, registers, ip):
        size = 2
        augmented_op, out_val = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        result_value = self.get_value(registers, out_val, param_modes[0])
        self.output_buffer.post(result_value)
        return ip + size

    def rel(self, registers, ip):
        size = 2
        augmented_op, rel_offset = self.get_inputs(registers, ip, size)
        param_modes = self.get_param_modes(augmented_op, size)
        self.relative_base += self.get_value(registers, rel_offset, param_modes[0])
        return ip + size


with open('input.txt') as f:
    input_string = f.read()

registers = [int(num) for num in re.sub("[^-0-9]", " ", input_string).split()]
movement_buffer = Buffer()
camera_output = Buffer()

robot = IntProgram(registers, movement_buffer, camera_output)

NORTH = ( 0, -1)
SOUTH = ( 0,  1)
EAST =  ( 1,  0)
WEST =  (-1,  0)

directions = [
  NORTH,
  SOUTH,
  WEST,
  EAST
]

SCAFFOLD = ord('#')
OPEN = ord('.')
NEW_LINE = ord('\n')
UP = ord('^')
DOWN = ord('v')
LEFT = ord('<')
RIGHT = ord('>')

robot_orientations = [UP, DOWN, LEFT, RIGHT]

tile_map = {}
scaffolds = set()
curr_pos = (0, 0)
robot_pos = None

minX = 9999
maxX = -9999
minY = 9999
maxY = -9999

while not robot.completed:
    robot.run()
    while not camera_output.is_empty():
        status = camera_output.get()
        if status == SCAFFOLD or status in robot_orientations:
            if status in robot_orientations:
                robot_pos = curr_pos
            tile_map[curr_pos] = status
            scaffolds.add(curr_pos)
            curr_pos = get_new_pos(curr_pos, EAST)
            continue
        elif status == OPEN:
            tile_map[curr_pos] = OPEN
            curr_pos = get_new_pos(curr_pos, EAST)
        elif status == NEW_LINE:
            curr_pos = (0, curr_pos[1] + 1)
        else:
            assert(0)
            continue
        minX = min(minX, curr_pos[0])
        maxX = max(maxX, curr_pos[0])
        minY = min(minY, curr_pos[1])
        maxY = max(maxY, curr_pos[1])

intersections = []
for pos in tile_map:
    if tile_map[pos] != SCAFFOLD:
        continue
    all_adjacents_scaffold = True
    for direction in directions:
        adjacent_pos = get_new_pos(pos, direction)
        if adjacent_pos not in tile_map or \
                tile_map[adjacent_pos] != SCAFFOLD:
            all_adjacents_scaffold = False
    if all_adjacents_scaffold:
        intersections.append(pos)

alignment = sum( pos[0] * pos[1] for pos in intersections)
print(alignment)

path = ""
visited = set()
while len(visited) != len(scaffolds):
    for move in directions:
        adjacent_pos = get_new_pos(robot_pos)