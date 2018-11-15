import random
num = 5
def is_prime(n):
	assert n >= 2
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	s = 0
	d = n - 1
	while True:
		quotient, remander = divmod(d,2)
		if remander == 1:
			break
		s += 1
		d = quotient
	assert 2 ** s *d == n-1
	def composite(a):
		if pow(a,d,n) == 1:
			return False
		for i in range(s):
			if pow(a,2**i*d,n) == n-1:
				return False
		return True
	for i in range(num):
		a = random.randrange(2,n)
		if composite(a):
			return False
	return True
def gcd(a, b):
	while b:
 		a, b = b, a % b
	return a
if __name__ == "__main__":
	#n = int(raw_input("Nhap n:"))
	n = pow(2,23872811111)
	print(is_prime(n))
	print(gcd(2558,6665))

