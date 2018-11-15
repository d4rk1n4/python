import sympy

arr = list(sympy.primerange(2,200))

for i in arr:
	if (sympy.isprime(2**i-1)):
		print sympy.prevprime(2**i-1)