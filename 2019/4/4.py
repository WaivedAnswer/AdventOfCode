import re


def two_repeats(possible_pass):
    return re.search(r"(\d)\1", possible_pass) is not None


def exactly_two_repeats(possible_pass):
    matches = re.finditer(r"(\d)\1+", possible_pass)
    are_exactly_two_matches = [len(match.group()) == 2 for match in matches]
    return any(are_exactly_two_matches)


def pass_sorted(possible_pass):
    sort_pass = "".join(sorted(possible_pass, key=lambda c: int(c)))
    return possible_pass == sort_pass


def part1(lower_bound, upper_bound):
    return sum(1 for password in range(lower_bound, upper_bound)
               if pass_sorted(str(password)) and two_repeats(str(password)))


def part2(lower_bound, upper_bound):
    return sum(1 for password in range(lower_bound, upper_bound)
               if pass_sorted(str(password)) and exactly_two_repeats(str(password)))


print(part1(108457, 562041 + 1))
print(part2(108457, 562041 + 1))
