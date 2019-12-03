import Common
import random


def run_int_program(int_string, noun, verb):
    numbers = Common.numbers(int_string)
    numbers[1] = noun
    numbers[2] = verb

    index = 0
    while True:
        if numbers[index] == 1:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
        elif numbers[index] == 2:
            numbers[numbers[index + 3]] = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
        elif numbers[index] == 99:
            break
        index += 4
    return numbers[0]


def part2(int_string):
    while True:
        rand_noun = random.randint(0, 100)
        rand_verb = random.randint(0, 100)

        if run_int_program(int_string, rand_noun, rand_verb) == 19690720:
            break

    print(100 * rand_noun + rand_verb)


def part1(int_string):
    base_noun = 12
    base_verb = 2
    print(run_int_program(int_string, base_noun, base_verb))


input_string = Common.inputAsString()

part1(input_string)
part2(input_string)
