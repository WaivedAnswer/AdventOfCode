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


def inp(registers, ip):
    size = 2
    augmented_op, result = get_inputs(registers, ip, size)
    in_val = int(input("Input a number: "))
    registers[result] = in_val
    return ip + size

def out(registers, ip):
    size = 2
    augmented_op, out_val_pos = get_inputs(registers, ip, size)
    print("Output: ", registers[out_val_pos])
    return ip + size

instructions = {
    1: add,
    2: mult,
    3: inp,
    4: out
}

def run_int_program(int_string, noun, verb):
    numbers = Common.numbers(int_string)

    index = 0
    while True:
        op_code = get_op_code(numbers[index])
        if op_code == 99:
            break
        elif op_code in instructions:
            index = instructions[op_code](numbers, index)


def part1(int_string):
    base_noun = 12
    base_verb = 2
    return run_int_program(int_string, base_noun, base_verb)

print(get_op_code(1002) == 2)
print(get_param_mode(1002, 0) == 0)
print(get_param_mode(1002, 1) == 1)
input_string = Common.inputAsString()

print(part1(input_string))
#print(part2(input_string) == 5398)
