def score(name):
	sum = 0
	for letter in name:
		sum += (ord(letter) - ord('A') + 1)
	return sum

with open('022_names.txt', 'r') as file:
	names = sorted(file.read().replace('"', '').split(','))

	sum = 0
	for i in range(len(names)):
		sum += (i + 1) * score(names[i])
	print(sum)
