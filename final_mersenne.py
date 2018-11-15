
from random import randrange, getrandbits
from itertools import repeat
import sympy

#Miller-Rabin
def isPrime(n, t = 7):
    
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

#Mersenne list without 3
def MersenneNumber(n):
	temp = ( 2**j - 1 for j in range(3,1234,2) if isPrime(j) and isPrime(2**j-1)) 
	return [temp.next() for i in range(n)]

# temp = ( 2**j - 1 for j in range(3,1234,2) if sympy.isprime(j) and sympy.isprime(2**j-1)) 

if __name__ == "__main__":
	print "(Greatest prime smaller than first n Mersenne primes)"
	n = input("n (n < 15) = ")
	A = [3]
	A += MersenneNumber(n - 1)
	for i in A:
		print sympy.prevprime(i)