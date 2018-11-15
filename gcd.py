
def gcd(a,b):
	while b:
		a, b = b, a % b
	return a

# a^p % n
def module(a, p, n):
	result = 1
	a = a % n
	while(p > 0):
		#p is odd
		if ((p & 1) == 1):
			result = (result * a) % n
		#p/2
		p = p >> 1
		a = (a * a ) % n	
	return result

if __name__ == '__main__':
	print "1. gcd a  b."
	print "2. Mod a^b % n"
		
	while True:
		k = input("Enter k : ")	
		if (k == 1):
			a = input("a = ")
			b = input("b = ")
			print gcd(a,b)
		if (k == 2):
			a = input("a = ")
			b = input("b = ")
			n = input("n = ")
			print module(a,b,n)
		if (k > 2):
			break	
	

