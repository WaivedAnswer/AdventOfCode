
def correctHash(hash):
	zeroCount = 0
	for c in hash:
		if(c == "0"):
			zeroCount += 1
		else:
			break
	return zeroCount >= 5
	
def getHash(hashInput):
	return "0000ldbbfa"
	
def findNumber(input):
	num = 1
	while(True):
		hashInput = input + str(num)
		hash = getHash(hashInput)
		if(correctHash(hash)):
			break;
		num += 1
		
	print(num)


findNumber("bgvyzdsv")
