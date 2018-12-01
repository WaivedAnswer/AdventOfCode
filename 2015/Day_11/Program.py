

def incrementChar(char):
	if(char == "z" or char == "Z"):
		return "a"
	return chr(ord(char) + 1)

def incrementedWord(word):
	return incrementedWordAtIndex(word, -1)
	
def incrementedWordAtIndex(word,index):
	if(word[index] == "z" or word[index] == "Z" ):
		if(index == 0 or len(word) == 1 ):
			return "a" * (len(word) + 1)
		else:
			return incrementedWordAtIndex(word, index - 1)
	newWord = word[:index] + incrementChar(word[index])
	if(index > 0):
		newWord = newWord + "a" * len(word[index+1:])
	else:
		newWord = newWord + "a" * len(word[len(word)+index+1:])
	return newWord
	
def passes_ruleset(password, ruleSet):
	for rule in ruleSet:
		if not rule.passes(password):
			return False
	return True

#class rule:
#	def passes(password):
#		return False
#	def get_next(password):
#		return password

class disallowedCharsRule:
	def __init__(self, disallowedChars):
		self.disallowed = disallowedChars
		
	def passes(self, password):
		for d in self.disallowed:
			if d in password:
				return False
		return True
	
	def get_next(self, password):
		next = password
		for i,c in enumerate(password):
			if c in self.disallowed:
				next = incrementedWordAtIndex(next, i)
				break
		return next
		
class doubleCharsRule:
		
	def passes(self, password):
		lastc = ""
		matches = []
		for c in password:
			if( c == lastc):
				matches.append(c)
				lastc = ""
			else:
				lastc = c
			if(len(matches) == 2):
				return True
				
		return False
	#likely better way for this one
	def get_next(self, password):
		next = password
		while not self.passes(next):
			next = incrementedWord(next)
		return next
		
class consecutiveCharsRule:
		
	def passes(self, password):
		charStack = []
		for c in password:
			if(len(charStack) >= 3):
				charStack.pop(0)
			charStack.append(c)
			if(len(charStack) == 3):
				ints = [ord(i) for i in charStack ]
				if (ints[1] == ints[0] + 1) and (ints[2] == ints[0] + 2):
					return True
		return False
		
	#likely better way for this one
	def get_next(self, password):
		next = password
		while not self.passes(next):
			next = incrementedWord(next)
		return next
		
def passes_ruleset(password, ruleset):
	for rule in ruleset:
		if(not rule.passes(password)):
			return False
	return True
	
def getNextPass(current):
	new = current
	ruleSet = [disallowedCharsRule(["i", "l", "o"]), consecutiveCharsRule(), doubleCharsRule() ]
	while not passes_ruleset(new, ruleSet):
		for rule in ruleSet:
			new = rule.get_next(new)
	return new
			
assert(incrementedWord("a") == "b")
assert(incrementedWord("z") == "aa")
assert(incrementedWord("az") == "ba")
assert(disallowedCharsRule(["i", "l", "o"]).get_next("ghijklmn") == "ghjaaaaa")
assert(disallowedCharsRule(["i", "l", "o"]).passes("ghjaaaaa"))
assert(not disallowedCharsRule(["i", "l", "o"]).passes("ghijklmn"))
print("Disallowed passed")

assert(doubleCharsRule().passes("abcdffaa"))
assert(doubleCharsRule().get_next("abcdefgh") == "abcdffaa")
print("Doubles passed")

assert(consecutiveCharsRule().passes("hijklmmn"))
assert(consecutiveCharsRule().get_next("hikzzzzz") == "hilaaabc")
print("Consecutives passed")

assert(getNextPass("abcdefgh") == "abcdffaa")
print("Passed First")
assert(getNextPass("ghijklmn") == "ghjaabcc")
print("Passed Second")

print(getNextPass("hepxcrrq"))
print(getNextPass(incrementedWord(getNextPass("hepxcrrq"))))