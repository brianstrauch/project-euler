def leap_year(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False	

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1 # monday

# 1900
for d in days:
	day = (day + d) % 7

# 1901 - 2000
sundays = 0
for year in range(1901, 2001):
	if leap_year(year):
		days[1] = 29
	else:
		days[1] = 28

	for d in days:
		if day == 0:
			sundays += 1
		day = (day + d) % 7

print(sundays)
