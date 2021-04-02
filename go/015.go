package main

import (
	"fmt"
	"math/big"
)

func main() {
	n := factorial(40)
	d := factorial(20)

	n.Div(n, d)
	n.Div(n, d)

	fmt.Println(n)
}

func factorial(n int) *big.Int {
	f := big.NewInt(1)
	for i := 2; i <= n; i++ {
		f.Mul(f, big.NewInt(int64(i)))
	}
	return f
}
