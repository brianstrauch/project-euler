ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

letters = 0
for n in range(1, 1001):
	t = n
	word = ''

	# thousands
	if t == 1000:
		word += 'onethousand'
		t = t % 1000
	
	# hundreds
	if t >= 100:
		word += ones[t // 100] + 'hundred'
		if t % 100 > 0:
			word += 'and'
		t = t % 100

	# tens
	if t >= 20:
		word += tens[t // 10]
		t = t % 10
	elif t >= 10:
		word += teens[t % 10]
		t = 0

	# ones
	if t > 0:
		word += ones[t]

	letters += len(word)

print(letters)
