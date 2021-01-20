n = 100000

is_prime = [True] * n
is_prime[0] = False
is_prime[1] = False
for i in range(2, n):
    if is_prime[i]:
        for j in range(i * 2, n, i):
            is_prime[j] = False

longest = (0, 0)

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        x = 0
        while True:
            y = x * x + a * x + b
            if y < 0 or not is_prime[y]:
                break
            x += 1
        x -= 1
        
        if x > longest[0]:
            longest = (x, a * b)

print(longest[1])
