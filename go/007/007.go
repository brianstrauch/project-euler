package main

import "fmt"

func main() {
	n := 1000000

	isPrime := make([]bool, n)
	for i := 0; i < n; i++ {
		isPrime[i] = true
	}

	count := 0

	for i := 2; i < n; i++ {
		if isPrime[i] {
			for j := 2 * i; j < n; j += i {
				isPrime[j] = false
			}

			count++
			if count == 10001 {
				fmt.Println(i)
				break
			}
		}
	}
}
