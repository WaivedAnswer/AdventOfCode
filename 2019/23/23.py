import Common
from collections import defaultdict
from queue import Queue
from threading import Thread, Lock


def get_op_code(augmented_op):
    return augmented_op % 100


def get_new_pos(old_pos, move_vector):
    return tuple(dim + move for dim, move in zip(old_pos, move_vector))


class MultiBuffer:
    def __init__(self):
        self.buffers = defaultdict(list)
        self.completed = set()
        self.nat = [None, None]
        self.x_y = 0
        self.first = True
        self.idle = {}
        self.reset_idles()
        self.sent = set()
        self.lock = Lock()

    def reset_idles(self):
        for i in range(50):
            self.idle[i] = False

    def _set_nat(self, val):
        if self.first and self.x_y == 1:
            print("Part 1:", val)
            self.first = False

        self.nat[self.x_y] = val
        self.x_y = (self.x_y + 1) % 2

    def _post_nat(self):
        print("Post:", self.nat)
        self.reset_idles()
        self.post(self.nat[0], 0)
        self.post(self.nat[1], 0)
        if self.nat[1] in self.sent:
            print("Part2:", self.nat[1])
        self.sent.add(self.nat[1])

    def post(self, val, dest_id):
        if dest_id == 255:
            self._set_nat(val)

        self.buffers[dest_id].append(val)

    def is_empty(self, dest_id):
        return len(self.buffers[dest_id]) == 0

    def get(self, dest_id):
        with self.lock:
            if all(self.idle.values()):
                self._post_nat()
        if self.is_empty(dest_id):
            self.idle[dest_id] = True
            return -1
        self.idle[dest_id] = False
        return self.buffers[dest_id].pop(0)

    def complete(self, dest_id):
        if dest_id in self.buffers:
            self.completed.add(dest_id)

    def join(self):
        while len(self.completed) != 50:
            pass


class PacketBuffer:
    def __init__(self, delegate_buffer):
        self.buffer = []
        self.delegate_buffer = delegate_buffer

    def post(self, val):
        self.buffer.append(val)
        if len(self.buffer) == 3:
            dest_address, x, y = self.buffer
            self.delegate_buffer.post(x, dest_address)
            self.delegate_buffer.post(y, dest_address)
            self.buffer.clear()


class IntProgram(Thread):
    def __init__(self, registers, input_buffer, output_buffer, program_id):
        Thread.__init__(self)
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
        for idx, initial_value in enumerate(registers):
            self.registers[idx] = initial_value
        self.relative_base = 0
        self.index = 0
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer
        self.completed = False
        self.program_id = program_id

    def run(self):
        while True:
            op_code = get_op_code(self.registers[self.index])
            if op_code == 99:
                self.completed = True
                self.input_buffer.complete(self.program_id)
                break
            elif op_code in self.instructions:
                instruction = self.instructions[op_code]
                old_index = self.index
                self.index = instruction(self.registers, self.index)
                assert(old_index != self.index)
            else:
                assert 0

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
        in_val = self.input_buffer.get(self.program_id)
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

initial_registers = Common.numbers(input_string)

multibuffer = MultiBuffer()

computers = []

for computer_id in range(50):
    computer = IntProgram(initial_registers, multibuffer, PacketBuffer(multibuffer), computer_id)
    computers.append(computer)
    multibuffer.post(computer_id, computer_id)

for computer in computers:
    computer.start()

multibuffer.join()
