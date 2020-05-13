package main

import "fmt"

func main() {
	ans := 0
	for a := 100; a < 1000; a++ {
		for b := a; b < 1000; b++ {
			c := a * b
			if isPalindrome(c) && c > ans {
				ans = c
			}
		}
	}
	fmt.Println(ans)
}

func isPalindrome(n int) bool {
	return n == reverse(n)
}

func reverse(n int) int {
	r := 0
	for n > 0 {
		r = 10 * r + n % 10
		n /= 10
	}
	return r
}
