#!/usr/bin/env python3#
import Common


def nextIndex(currIndex, offset, array):
    return (currIndex + offset) % len(array)

def getDigits(num):
    return [int(c) for c in str(num)]
    
def part1(input):
    finalRecipe = input + 10
    elf1 = 0
    elf2 = 1
    recipes = [3,7]
    while(len(recipes) <= finalRecipe - 1):
        nextRecipeSum = recipes[elf1] + recipes[elf2]
        recipes.extend(getDigits(nextRecipeSum))
        elf1 = nextIndex(elf1, 1 + recipes[elf1], recipes)
        elf2 = nextIndex(elf2, 1 + recipes[elf2], recipes)
    return "".join([str(c) for c in recipes[input:input + 10]])
    

    
def part2(input):
    elf1 = 0
    elf2 = 1
    recipes = [3,7]
    
    while True:
        nextRecipeSum = recipes[elf1] + recipes[elf2]
        recipes.extend(getDigits(nextRecipeSum))
        elf1 = nextIndex(elf1, 1 + recipes[elf1], recipes)
        elf2 = nextIndex(elf2, 1 + recipes[elf2], recipes)
        if("".join([str(c) for c in recipes[-len(input):]]) == input):
            break
        
    return len(recipes) - len(input)
    
def part2_2(input):
    elf1 = 0
    elf2 = 1
    recipes = [3,7]
    
    digits = getDigits(input)
    
    while True:
        nextRecipeSum = recipes[elf1] + recipes[elf2]
        recipeDigits = getDigits(nextRecipeSum)
        
        recipes.append(recipeDigits[0])
        
        if(recipes[-len(digits):] == digits):
            break
            
        if(nextRecipeSum >= 10):
            recipes.append(recipeDigits[1])
            
        elf1 = nextIndex(elf1, 1 + recipes[elf1], recipes)
        elf2 = nextIndex(elf2, 1 + recipes[elf2], recipes)
        
        if(recipes[-len(digits):] == digits):
            break
        
    return len(recipes) - len(digits)
            
input = Common.inputAsLines()
#input = Common.inputAsString()

assert(part1(9) == "5158916779")
assert(part1(5) == "0124515891")
assert(part1(18) == "9251071085")
assert(part1(2018) == "5941429882")
print(part1(652601))

assert(part2_2(515891) == 9)
#assert(part2_2(01245) == 5)
assert(part2_2(92510) == 18)
print(part2_2(59414))
assert(part2_2(59414) == 2018)
print("TestsPassed")
print(part2_2(652601))




