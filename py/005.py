def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

def lcm(a, b):
	return a * b / gcd(a, b)

n = 1
for i in range(1, 20):
	n = lcm(n, i)
print(n)
