package main

import (
	"fmt"
	"math/big"
)

func main() {
	n_2 := big.NewInt(1)
	n_1 := big.NewInt(1)
	var lim big.Int
	lim.Exp(big.NewInt(10), big.NewInt(999), nil)
	index := 2
	for {
		index++
		n_2.Add(n_2, n_1)
		if n_2.Cmp(&lim) == 1 {
			break
		}
		n_2, n_1 = n_1, n_2
	}
	fmt.Println(index) // 4782
	// Spoiled by Python's handling of arbitrary length integers...
}
