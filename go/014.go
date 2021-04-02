package main

import "fmt"

func main() {
	longest := 0
	idx := 0

	for i := 1; i < 1000000; i++ {
		n := i

		count := 1
		for n > 1 {
			if n%2 == 0 {
				n /= 2
			} else {
				n = 3*n + 1
			}
			count++
		}

		if count > longest {
			longest = count
			idx = i
		}
	}

	fmt.Println(idx)
}
