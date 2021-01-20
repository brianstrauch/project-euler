longest = (1, 0)

for d in range(2, 1000):
    states = {}

    i, n = 0, 1
    while n > 0:
        x = (10 * n) // d

        if (n, x) in states:
            cycle = i - states[(n, x)]
            if cycle > longest[0]:
                longest = (cycle, d)
            break
        states[(n, x)] = i

        n = 10 * n - x * d
        i += 1

print(longest[1])