import Common

def has_required_vowels(input):
	vowelCount = 0
	for vowel in "aeiou":
		vowelCount += input.count(vowel)
	return vowelCount >=3
	
def has_double_letter(input):
	if(len(input) < 2):
		return False
	for i in range(len(input)-1):
		firstLetter = input[i]
		secondLetter = input[i+1]
		if(firstLetter == secondLetter):
			return True
	return False
	
def has_invalid_strings(input):
	invalidStrings = ["ab", "cd", "pq", "xy"]
	for invalid in invalidStrings:
		if invalid in input:
			return True
	return False

def is_nice_string(input):
	lower = input.lower()
	if( not has_required_vowels(lower)):
		return False
	if( not has_double_letter(lower)):
		return False
	if( has_invalid_strings(lower)):
		return False
	
	return True
	
def has_repeating_pair(input, pair):
	splitString = input.split(pair)
	return len(splitString) > 2
	
def has_repeating_pairs(input):
	for i in range(len(input) - 1):
		pair = input[i:i+2]
		if( has_repeating_pair(input, pair)):
			return True
	return False
	
def has_mini_anagram(input):
	for i in range(len(input) - 2):
		trio = input[i:i+3]
		if( trio == trio[::-1]):
			return True
	return False
	
	
def is_nice_string2(input):
	lower = input.lower()
	
	if( not has_repeating_pairs(lower)):
		return False
		
	if( not has_mini_anagram(lower)):
		return False
		
	return True

def count_nice_strings(input, nice_string_op):
	count = 0
	for line in input:
		if(nice_string_op(line)):
			count = count + 1
	return count
	

input = Common.inputAsLines()

assert(is_nice_string("aaa") == True)
assert(is_nice_string("ugknbfddgicrmopn") == True)
assert(is_nice_string("jchzalrnumimnmhp") == False)
assert(is_nice_string("haegwjzuvuyypxyu") == False)
assert(is_nice_string("dvszwmarrgswjxmb") == False)

assert(is_nice_string2("qjhvhtzxzqqjkmpb") == True)
assert(is_nice_string2("xxyxx") == True)
assert(is_nice_string2("uurcxstgmygtbstg") == False)
assert(is_nice_string2("ieodomkazucvgmuy") == False)

print(count_nice_strings(input, is_nice_string))
print(count_nice_strings(input, is_nice_string2))