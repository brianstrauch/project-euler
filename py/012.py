from math import sqrt

def divisors(n):
	count = 1
	i = 0
	while primes[i] <= n:
		repetitions = 0
		while n % primes[i] == 0:
			n /= primes[i]
			repetitions += 1
		count *= (repetitions + 1)
		i += 1
	return count

P, primes = [True] * 1000000, []
for i in range(2, len(P)):
	if P[i]:
		primes.append(i)
		for j in range(2 * i, len(P), i):
			P[j] = False

n, i = 1, 1
while divisors(n) <= 500:
	i += 1
	n += i
print(n)
