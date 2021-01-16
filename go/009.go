package main

import "fmt"

func main() {
	n := 1000

	for a := 1; a < n; a++ {
		for b := a; b < n; b++ {
			c := n - (a + b)
			if a*a+b*b == c*c {
				fmt.Println(a * b * c)
				return
			}
		}
	}
}
