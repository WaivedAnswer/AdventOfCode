#!/usr/bin/env python3#
import Common
import os
from collections import defaultdict
from enum import Enum
import time



turnOrder = ["l", "s", "r"]

cartDirections = ["<", "^", ">", "v"]
straights = ["|", "-"]
curves = ["/", "\\"]
intersection = "+"


def getIntersectionDirection(currDirection, lastTurn):
	if lastTurn == None:
		nextIndex = 0
	else:
		nextIndex = (turnOrder.index(lastTurn) + 1) % len(turnOrder)
	
	turn = turnOrder[nextIndex]
	
	if turn == "s":
		return currDirection, turn
	elif turn == "l":
		nextDirection = (cartDirections.index(currDirection) - 1) % len(cartDirections)
		return (
			cartDirections[nextDirection],
			turn
		)
	elif turn == "r":
		nextDirection = (cartDirections.index(currDirection) + 1) % len(cartDirections)
		return (
			cartDirections[nextDirection],
			turn
		)
	assert(False)
	return None


def getCurveDirection(currDirection, curve):
	if currDirection == "^" or currDirection == "v":
		if curve == "\\":
			return cartDirections[
				(cartDirections.index(currDirection) - 1) % len(cartDirections)
			]
		elif curve == "/":
			return cartDirections[
				(cartDirections.index(currDirection) + 1) % len(cartDirections)
			]
	elif currDirection == "<" or currDirection == ">":
		if curve == "\\":
			return cartDirections[
				(cartDirections.index(currDirection) + 1) % len(cartDirections)
			]
		elif curve == "/":
			return cartDirections[
				(cartDirections.index(currDirection) - 1) % len(cartDirections)
			]
	assert(False)
	return None

def movePos(row,col,currDirection):
	if currDirection == "<":
		col -= 1
	elif currDirection == ">":
		col += 1
	elif currDirection == "^":
		row -= 1
	elif currDirection == "v":
		row += 1
	else:
		assert(False)
	return row,col

def getCartMovePos(row, col, currDirection, lastTurn, coords):
	row, col = movePos(row,col,currDirection)
	
	if coords[row][col] in straights:
		return (row, col, currDirection, lastTurn)
	elif coords[row][col] == intersection:
		newDirection, newTurnIndex = getIntersectionDirection(
			currDirection, lastTurn
		)
		return (row, col, newDirection, newTurnIndex)
	elif coords[row][col] in curves:
		newDirection = getCurveDirection(currDirection, coords[row][col])
		return (row, col, newDirection, lastTurn)
		
	assert(False)
	return row, col, currDirection, lastTurn


def printGrid(coords, carts):
	clear = lambda: os.system("cls")
	#clear()
	for i in range(len(coords)):
		for j in range(len(coords[i])):
			tup = (i,j)
			if tup in carts:
				cart = carts[tup]
				print(cart[0], end="")
			else:
				print(coords[i][j], end="")
		print("")

def sortItems(itemDict, width):
	return sorted(itemDict.items(), key=lambda item: item[0][0] * width + item[0][1])

def part1(input):
	coords = []
	carts = defaultdict(tuple)
	
	for i, line in enumerate(input):
		coords.append([])
		for j, c in enumerate(line):
			if c in cartDirections:
				carts[(i, j)] = (c, None)
				if c == "^" or c == "v":
					coords[i].append("|")
				elif c=="<" or c==">":
					coords[i].append("-")
			else:
				coords[i].append(c)
	
	ticks = 0
	crash = None
	while not crash:
		newCarts = defaultdict(tuple)
		processed = {}
		for cartPos, cart in sortItems(carts, len(coords)):
			row, col, direction, lastTurn = getCartMovePos(cartPos[0], cartPos[1], cart[0], cart[1], coords)
			if ((row, col) in newCarts) or ((row,col) in carts and (row,col) not in processed):
				crash = (col, row)
				break
			newCarts[(row, col)] = (direction, lastTurn)
			processed[cartPos] = True
		carts = newCarts
		ticks += 1
		#time.sleep(0.5)
		#printGrid(coords, carts)
	return crash
	
def part2(input):
	coords = []
	carts = defaultdict(tuple)
	
	for i, line in enumerate(input):
		coords.append([])
		for j, c in enumerate(line):
			if c in cartDirections:
				carts[(i, j)] = (c, None)
				if c == "^" or c == "v":
					coords[i].append("|")
				elif c=="<" or c==">":
					coords[i].append("-")
			else:
				coords[i].append(c)
	
	ticks = 0
	while len(carts) > 1:
		newCarts = defaultdict(tuple)
		processed = {}
		crashed = []
		for cartPos, cart in sortItems(carts, len(coords)):
			row, col, direction, lastTurn = getCartMovePos(cartPos[0], cartPos[1], cart[0], cart[1], coords)
			if (row, col) in newCarts:
				crashed.append((row,col))
			elif (row,col) in carts and (row,col) not in processed:
				otherRow, otherCol, otherDirection, otherLastTurn = getCartMovePos(row, col, carts[(row,col)][0], carts[(row,col)][1], coords)
				crashed.append((otherRow,otherCol))
				crashed.append((row,col))

			newCarts[(row, col)] = (direction, lastTurn)
			processed[cartPos] = True
		for crash in crashed:
			del newCarts[crash]
		carts = newCarts
		ticks += 1
		#time.sleep(0.5)
		#printGrid(coords, carts)
	
	return [ (cart[1],cart[0]) for cart in carts ][0]


input = Common.inputAsLines()
# input = Common.inputAsString()



print(part1(input))
print(part2(input))
