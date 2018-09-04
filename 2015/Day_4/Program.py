import hashlib

def isCorrectHash(hash, count):
	zeroCount = 0
	for c in hash:
		if(c == "0"):
			zeroCount += 1
		else:
			break
	return zeroCount >= count
	
def getHash2(input):
	m = hashlib.md5()
	m.update(input.encode('utf-8'))
	return m.hexdigest()

	
def findNumber(input):
	num = 1
	while(True):
		hashInput = input + str(num)
		hash = getHash2(hashInput)
		if(isCorrectHash(hash, 5)):
			break;
		num += 1
		
	return num
	
def findNumber6(input):
	num = 1
	while(True):
		hashInput = input + str(num)
		hash = getHash2(hashInput)
		if(isCorrectHash(hash, 6)):
			break;
		num += 1
		
	return num
	
#assert(getHash2("") == "d41d8cd98f00b204e9800998ecf8427e")
#assert( getHash2("abcdef609043").startswith("000001dbbfa"))
#print(str(getHash2("")))
#print("Hash Passes")
#
#assert( findNumber("abcdef") == 609043)
#assert( findNumber("pqrstuv") == 1048970)

print (findNumber6("bgvyzdsv"))