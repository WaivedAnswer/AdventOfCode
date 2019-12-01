import Common

line_input = Common.inputAsLines()


def calc_fuel(mass):
    return int(mass / 3) - 2


def calc_fuel_recursive(mass):
    fuel = calc_fuel(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel_recursive(fuel)


mass_sum = 0
recursive_sum = 0
for line in line_input:
    mass = int(line)
    mass_sum += calc_fuel(mass)
    recursive_sum += calc_fuel_recursive(mass)

print(mass_sum)
print(recursive_sum)