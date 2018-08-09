index, a, b = 1, 1, 1
while len(str(a)) < 1000:
	a, b = b, a + b
	index += 1
print(index)
