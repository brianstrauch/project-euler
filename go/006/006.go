package main

import "fmt"

func main() {
	sum := 0
	sumOfSquares := 0

	for i := 1; i <= 100; i++ {
		sum += i
		sumOfSquares += i * i
	}

	squareOfSum := sum * sum
	fmt.Println(squareOfSum - sumOfSquares)
}
