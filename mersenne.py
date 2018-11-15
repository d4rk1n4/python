from random import randrange, getrandbits
from itertools import repeat

def isPrime(n, t = 7):
    """Miller-Rabin primality test"""
    
    def isComposite(a):
        """Check if n is composite"""
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    assert n > 0
    if n < 3:   
        return [False, True][n]
    elif not n & 1:
        return False
    else:
        s, d = 0, n - 1
        while not d & 1:
            s += 1
            d >>= 1
    for _ in repeat(None, t):
        if isComposite(randrange(2, n)):
            return False
    return True

#find prime between m and n-2 with n is prime
def largestPrimes(m,n):
	for k in range(n - 2, m, -2):
		if isPrime(k):
			return k
			break

def MersenneNumber(n):
	temp = ( 2**j - 1 for j in range(3,1324,2) if isPrime(j) and isPrime(2**j-1)) 
	return [temp.next() for v in range(n)]

if __name__ == "__main__":
	n = input("n: ")
	A = [3]
	A += MersenneNumber(n - 1)

	for i in A:
		print i
		
	for i in range(n):
		print largestPrimes(A[i],A[i+1])
	