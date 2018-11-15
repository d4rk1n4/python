
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

def getPrime(n):
    """Get a n-bit prime"""  
    p = getrandbits(n)
    while not isPrime(p):
        p = getrandbits(n)     
    return p    
    
if __name__ == "__main__":
    # check a is prime
    a = input(" a = ")
    print(isPrime(a))
      
    # get a random prime p bits long
    p = input("bits b : ")
    print(getPrime(p))