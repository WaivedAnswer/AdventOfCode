#!/usr/bin/env python#
import Common
from collections import defaultdict


def distFromOrigin(x, y):
    return manhattanDist(x, y, 0, 0)


def manhattanDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def countClosest(coords, names):
    closest = defaultdict(lambda: [])
    minX = min(coords, key=lambda x: x[0])[0]
    minY = min(coords, key=lambda x: x[1])[1]
    maxX = max(coords, key=lambda x: x[0])[0]
    maxY = max(coords, key=lambda x: x[1])[1]
    coordTotals = defaultdict(int)
    infiniteAreas = set()
    for i in range(minX - 1, maxX + 1):
        for j in range(minY - 1, maxY + 1):
            dists = {p: manhattanDist(p[0], p[1], i, j) for p in coords}
            close = min(dists.items(), key=lambda p: p[1])
            minDist = close[1]
            if list(dists.values()).count(minDist) > 1:
                continue
            if (i == minX or i == maxX or j == minY or j == maxY) and list(
                dists.values()
            ).count(minDist) == 1:
                infiniteAreas.update(
                    {names[k] for k, d in dists.items() if d == minDist}
                )

            coordTotals[close[0]] += 1
    coordTotals = {
        key: total
        for (key, total) in coordTotals.items()
        if names[key] not in infiniteAreas
    }
    return Common.maxValuePair(coordTotals)


def regionCloseToAll(coords, minDist):
    closest = defaultdict(lambda: [])
    minX = min(coords, key=lambda x: x[0])[0]
    minY = min(coords, key=lambda x: x[1])[1]
    maxX = max(coords, key=lambda x: x[0])[0]
    maxY = max(coords, key=lambda x: x[1])[1]

    regionSum = 0
    for i in range(minX - 1, maxX + 1):
        for j in range(minY - 1, maxY + 1):
            dists = {p: manhattanDist(p[0], p[1], i, j) for p in coords}
            totalDist = sum([total for (key, total) in dists.items()])
            if totalDist < minDist:
                regionSum += 1
    return regionSum


def part1(input):
    names, coords = parseCoords(input)
    return countClosest(coords, names)


def parseCoords(input):
    coords = []
    names = {}
    coordName = "A"
    for line in input:
        numbers = Common.numbers(line)
        x = numbers[0]
        y = numbers[1]
        coords.append((x, y))
        names[(x, y)] = coordName
        coordName = chr(ord(coordName) + 1)
    return names, coords


def part2(input):
    names, coords = parseCoords(input)
    return regionCloseToAll(coords, 10000)


input = Common.inputAsLines()

print(part1(input))
print(part2(input))
