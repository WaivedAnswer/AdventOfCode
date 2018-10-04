def get_string_addition(chars):
	if(len(chars) == 0):
		return ""
	return str(len(chars))+chars[0]

def LookAndSay(strNum):
	newNum = ""
	charstack = []
	for char in strNum:
		if(len(charstack) == 0 or char == charstack[-1]):
			charstack.append(char)
		else:
			newNum+=get_string_addition(charstack)
			charstack.clear()
			charstack.append(char)
	
	newNum+=get_string_addition(charstack)
	charstack.clear()
	return newNum
	
def LookAndSayRepeat(strNum, repeatCount):
	repeat = strNum
	for i in range(repeatCount):
		repeat = LookAndSay(repeat)
	return repeat
		

assert( LookAndSay("1") == "11")
assert( LookAndSay("11") == "21")
assert( LookAndSay("21") == "1211")
assert( LookAndSay("1211") == "111221")
assert( LookAndSay("111221") == "312211")

print(len(LookAndSayRepeat("1113222113", 50)))
