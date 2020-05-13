package main

import "fmt"

func main() {
	n := 1
	for i := 1; i <= 20; i++ {
		n = lcm(n, i)
	}
	fmt.Println(n)
}

func lcm(a, b int) int {
	return a * b / gcd(a, b)
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a % b)
}

