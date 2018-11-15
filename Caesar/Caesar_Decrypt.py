import string
cipher = 'Gurer ner gjb xvaqf bs crbcyr va guvf jbeyq: gubfr jub ner ybbxvat sbe n ernfba naqgubfr jub ner svaqvat fhpprff. Gubfr jub ner ybbxvat sbe n ernfba nyjnlf frrxvat gurernfbaf jul gur jbex vf abg svavfurq. Naq crbcyr jub svaq fhpprff ner nyjnlf ybbxvat sbeernfbaf jul gur jbex pna or pbzcyrgrq.'
charset = string.letters + '0123456789'

def rot(st, k):
 	result = ""
 	for char in st:
 		if char in charset:
 			result += charset[(charset.index(char)-k)%26]
 		else:
 			result += char
 	return result
for k in range(26):
 	print k, rot(cipher, k)
