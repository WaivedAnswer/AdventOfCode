import Common


def get_op_code(augmented_op):
    return augmented_op % 100


def get_param_mode(augmented_op, param_num):
    divisor = pow(10, param_num + 2)
    mod = (augmented_op % (10 * divisor))
    return int(mod / divisor)


def get_inputs(registers, ip, size):
    return registers[ip: ip+size]


def get_value(registers, param_value, param_mode):
    if param_mode == 0:
        return registers[param_value]
    elif param_mode == 1:
        return param_value
    else:
        assert 0


def add(registers, ip):
    size = 4
    augmented_op, noun, verb, result = get_inputs(registers, ip, size)
    param_modes = [ get_param_mode(augmented_op, num) for num in range(size - 1)]
    registers[result] = get_value(registers, noun, param_modes[0]) + get_value(registers, verb, param_modes[1])
    return ip + size


def mult(registers, ip):
    size = 4
    augmented_op, noun, verb, result = get_inputs(registers, ip, size)
    param_modes = [get_param_mode(augmented_op, num) for num in range(size - 1)]
    registers[result] = get_value(registers, noun, param_modes[0]) * get_value(registers, verb, param_modes[1])
    return ip + size


def jmp_true(registers, ip):
    size = 3
    augmented_op, first, second = get_inputs(registers, ip, size)
    param_modes = [get_param_mode(augmented_op, num) for num in range(size - 1)]
    if get_value(registers, first, param_modes[0]) != 0:
        return get_value(registers, second, param_modes[1])
    else:
        return ip + size


def jmp_false(registers, ip):
    size = 3
    augmented_op, first, second = get_inputs(registers, ip, size)
    param_modes = [get_param_mode(augmented_op, num) for num in range(size - 1)]
    if get_value(registers, first, param_modes[0]) == 0:
        return get_value(registers, second, param_modes[1])
    else:
        return ip + size


def less_than(registers, ip):
    size = 4
    augmented_op, noun, verb, result = get_inputs(registers, ip, size)
    param_modes = [get_param_mode(augmented_op, num) for num in range(size - 1)]
    registers[result] = get_value(registers, noun, param_modes[0]) < get_value(registers, verb, param_modes[1])
    return ip + size


def equals(registers, ip):
    size = 4
    augmented_op, noun, verb, result = get_inputs(registers, ip, size)
    param_modes = [get_param_mode(augmented_op, num) for num in range(size - 1)]
    registers[result] = get_value(registers, noun, param_modes[0]) == get_value(registers, verb, param_modes[1])
    return ip + size


def inp(registers, ip):
    size = 2
    augmented_op, result = get_inputs(registers, ip, size)
    in_val = int(input("Input a number: "))
    registers[result] = in_val
    return ip + size


def out(registers, ip):
    size = 2
    augmented_op, out_val = get_inputs(registers, ip, size)
    param_modes = [get_param_mode(augmented_op, num) for num in range(size - 1)]
    print("Output: ", get_value(registers, out_val, param_modes[0]))
    return ip + size


class IntProgram:
    def __init__(self, instructions):
        self.instructions = instructions

    def run(self, registers):
        index = 0
        while True:
            op_code = get_op_code(registers[index])
            if op_code == 99:
                break
            elif op_code in self.instructions:
                instruction = self.instructions[op_code]
                index = instruction(registers, index)


def part1(registers):
    instructions = {
        1: add,
        2: mult,
        3: inp,
        4: out
    }
    program = IntProgram(instructions)
    return program.run(registers)

def part2(registers):
    instructions = {
        1: add,
        2: mult,
        3: inp,
        4: out,
        5: jmp_true,
        6: jmp_false,
        7: less_than,
        8: equals
    }
    program = IntProgram(instructions)
    return program.run(registers)


input_string = Common.inputAsString()
initial_registers = Common.numbers(input_string)

part1(initial_registers[:])
part2(initial_registers[:])
