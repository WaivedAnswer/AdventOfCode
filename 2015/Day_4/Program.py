from operator import ior;
import numpy as np;

def isCorrectHash(hash):
	zeroCount = 0
	for c in hash:
		if(c == "0"):
			zeroCount += 1
		else:
			break
	return zeroCount >= 5
	
def GetXor(input1, input2):
    return np.bitwise_xor(input1, input2)
	
def fromHex(input):
	return int(input, 16)
	
def getHash(hashInput):
	s = [0]*64
	K = [0]*64

	#s specifies the per-round shift amounts
	s[0:16] = [ 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22 ]

	s[16:32] = [ 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20 ]
                                                            
	s[32:48] = [ 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23 ]
                                                       
	s[48:64] = [ 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21 ]
	
	#(Or just use the following precomputed table):
	K[ 0: 4] = [ 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee ]
	K[ 4: 8] = [ 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501 ]
	K[ 8:12] = [ 0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be ]
	K[12:16] = [ 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821 ]
	K[16:20] = [ 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa ]
	K[20:24] = [ 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8 ]
	K[24:28] = [ 0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed ]
	K[28:32] = [ 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a ]
	K[32:36] = [ 0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c ]
	K[36:40] = [ 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70 ]
	K[40:44] = [ 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05 ]
	K[44:48] = [ 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665 ]
	K[48:52] = [ 0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039 ]
	K[52:56] = [ 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1 ]
	K[56:60] = [ 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1 ]
	K[60:64] = [ 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391 ]
	#Initialize variables:
	a0 = 0x67452301   #A
	b0 = 0xefcdab89   #B
	c0 = 0x98badcfe   #C
	d0 = 0x10325476   #D
	
	#Pre-processing: adding a single 1 bit
	#Pre-processing: padding with zeros
	originalLen = len(hashInput)
	hashInput += "1" 
	# Notice: the input bytes are considered as bits strings,
	#  where the first bit is the most significant bit of the byte.[48]
	

	#append "0" bit until message length in bits ≡ 448 (mod 512)
	while( len(hashInput) % 512 != 448):
		hashInput += "0"
	print(len(hashInput))
	#append original length in bits mod 2^64 to message
	hashInput += "0" * (originalLen % 2^64)
	print(len(hashInput))
	#Process the message in successive 512-bit chunks:
	for i in range(0, len(hashInput), 512):
		print("index")
		print (i)
		#break chunk into sixteen 32-bit words M[j], 0 <= j <= 15
		chunk = hashInput[i:i+512]
		print("-----")
		#print(chunk)
		M = [chunk[j:j + 32] for j in range(0, len(chunk), 32)]
		#Initialize hash value for this chunk:
		A = a0
		B = b0
		C = c0
		D = d0
		#Main loop:
		for t in range(0, 64):
			F = 0
			g = 0
			if 0 <= t and t <= 15:
				F = (B and C) or ((not B) and D)
				g = t
			elif 16 <= t and t <= 31:
				F = (D and B) or ((not D) and C)
				g = (5*t + 1) % 16
			elif 32 <= t and t  <= 47:
				F = GetXor(GetXor(B, C), D)
				g = (3*t + 5) % 16
			elif 48 <= t and t  <= 63:
				F = GetXor(C, (B or (not D)))
				g = (7*t) % 16
			#Be wary of the below definitions of a,b,c,d
			F = F + A + K[t] + fromHex(M[g])
			A = D
			D = C
			C = B
			B = B + leftrotate(F, s[t])
		#Add this chunk's hash to result so far:
		a0 = a0 + A
		b0 = b0 + B
		c0 = c0 + C
		d0 = d0 + D
		
	return hex(a0) + hex(b0) + hex(c0) + hex(d0) #(Output is in little-endian)
	
#leftrotate function definition
def leftrotate(x, c):
	return np.bitwise_or(x << c, x >> (32-c))
	
def findNumber(input):
	num = 1
	while(True):
		hashInput = input + str(num)
		hash = getHash(hashInput)
		if(isCorrectHash(hash)):
			break;
		num += 1
		
	return num


assert( findNumber("abcdef") == 609043)
assert( findNumber("pqrstuv") == 1048970)
print (findNumber("bgvyzdsv"))