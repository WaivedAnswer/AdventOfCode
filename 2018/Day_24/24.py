#!/usr/bin/env python3#
import Common
import re

class Group:
    def __init__(self, unit_count, hit_points, attack, initiative, weaknesses, immunities):
        self.unit_count = unit_count
        self.hit_points = hit_points
        self.attack = attack
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities

def parse_group(line):
    unit_count =

def part1(lines):
    is_immune_group = True
    for line in lines:
        if not line.strip():
            continue
        elif line.contains("Immune System"):
            is_immune_group = True
            continue
        elif line.contains("Infection"):
            is_immune_group = False
            continue
        else:
            group = parse_group(line)


lineInput = Common.inputAsLines()
print(part1(lineInput))




