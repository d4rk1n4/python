import string
plaintext ='The University of Information Technology'
charset = string.letters + '0123456789'

def rot(st, k):
 	result = ""
 	for char in st:
 		if char in charset:
 			result += charset[(charset.index(char)+k)%26]
 		else:
 			result += char
 	return result
for k in range(26):
 	print k, rot(plaintext, k)
