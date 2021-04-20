package main

import "fmt"

func main() {
	i := 1
	n := 1

	for {
		if countDivisors(n) > 500 {
			fmt.Println(n)
			break
		}

		i++
		n += i
	}
}

func countDivisors(n int) int {
	count := 1

	for i := 2; i <= n; i++ {
		power := 0
		for n%i == 0 {
			power++
			n /= i
		}
		count *= (power + 1)
	}

	return count
}
