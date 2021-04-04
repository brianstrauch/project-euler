package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n big.Int
	n.Exp(big.NewInt(2), big.NewInt(1000), big.NewInt(0))

	sum := big.NewInt(0)
	for n.Cmp(big.NewInt(0)) > 0 {
		var d big.Int
		d.Mod(&n, big.NewInt(10))
		sum.Add(sum, &d)
		n.Div(&n, big.NewInt(10))
	}

	fmt.Println(sum)
}
