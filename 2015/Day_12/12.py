import Common
import re

def sum_all_numbers(text):
    num_string = re.sub("[^-0-9]", " ", text)
    return sum([int(num) for num in num_string.split()])

def part2(text):
    total_sum = 0
    non_nested_pattern = re.compile(r"\{[^{}]+\}")
    red_pattern = re.compile(r":\"red\"")
    non_nested = non_nested_pattern.findall(text)
    if len(non_nested) == 0:
        return sum_all_numbers(text)

    for pattern in non_nested:
        print(pattern)
        if red_pattern.search(pattern) is None:
            total_sum += sum_all_numbers(pattern)
        else:
            print("miss")

    subbed_text = re.sub(non_nested_pattern, "", text)
    print(subbed_text)

    return total_sum + part2(subbed_text)

input_text = Common.inputAsString()
print(sum_all_numbers(input_text))
print(part2(input_text))