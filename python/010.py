prime = [True] * 2000000

sum = 0
for i in range(2, len(prime)):
	if prime[i]:
		for j in range(i, len(prime), i):
			prime[j] = False
		sum += i
print(sum)
