from math import sqrt

def prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

n = 1
primes = 0
while primes < 10001:
	n += 1
	if prime(n):
		primes += 1
print(n)
