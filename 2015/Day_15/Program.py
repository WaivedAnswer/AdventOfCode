import Common
import itertools

class Ingredient:
	def __init__(self, name, capacity, durability, flavor, texture, calories):
		self.name = name
		self.capacity = capacity
		self.durability = durability
		self.flavor = flavor
		self.texture = texture
		self.calories = calories
		
class Recipe:
	def __init__(self, ingredientAmounts):
		self.ingredientAmounts = ingredientAmounts
	
	def _normalize(self, score):
		if(score < 0):
			return 0
		return score
		
	def calorie_count(self):
		return sum([i.calories * self.ingredientAmounts[i] for i in self.ingredientAmounts.keys()])
	
	def score(self):
		capacity = 0
		durability = 0
		flavor = 0
		texture = 0
		
		for ingredient in self.ingredientAmounts.keys():
			capacity = capacity + self.ingredientAmounts[ingredient] * ingredient.capacity
			durability = durability + self.ingredientAmounts[ingredient] * ingredient.durability
			flavor = flavor + self.ingredientAmounts[ingredient] * ingredient.flavor
			texture = texture + self.ingredientAmounts[ingredient] * ingredient.texture
			
		capacity = self._normalize(capacity)
		durability = self._normalize(durability)
		flavor = self._normalize(flavor)
		texture = self._normalize(texture)
		
		return capacity * durability * flavor * texture
	

def parseIngredient(line):
	words = line.split()
	name = words[0].strip(":")
	capacity = int(words[2].strip(","))
	durability = int(words[4].strip(","))
	flavor = int(words[6].strip(","))
	texture = int(words[8].strip(","))
	calories = int(words[10])
	return Ingredient(name, capacity, durability, flavor, texture, calories)
	
def partition(n,k,l=1):
    '''n is the integer to partition, k is the length of partitions, l is the min partition element size'''
    if k < 1:
        return
    if k == 1:
        if n >= l:
            yield (n,)
        return
    for i in range(l,n//k+1):
        for result in partition(n-i,k-1,i):
            yield (i,)+result
	
def getBestRecipeScore(input, calorieCount = -1):
	ingredients = []
	for line in input:
		ingredients.append(parseIngredient(line))
	
	maxScore = 0
	for p in partition(100,len(ingredients)):
		for perm in itertools.permutations(p):
			ingredientAmounts = {}
			for idx,ingredient in enumerate(ingredients):
				ingredientAmounts[ingredient] = perm[idx]
			recipe = Recipe(ingredientAmounts)
			if(calorieCount != -1 and recipe.calorie_count() != calorieCount):
				continue
			score = recipe.score()
			if(score > maxScore):
				maxScore = score
	return maxScore

assert(getBestRecipeScore(["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
"Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"]) == 62842880)
input = Common.inputAsLines()
print(getBestRecipeScore(input))
print(getBestRecipeScore(input, 500))