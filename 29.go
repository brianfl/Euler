package main

import (
	"fmt"
	"math/big"
)

func main() {
	m := make(map[string]bool)
	for i := 2; i <= 100; i++ {
		for j := 2; j <= 100; j++ {
			i_f := big.NewInt(int64(i))
			j_f := big.NewInt(int64(j))
			var val big.Int
			val.Exp(i_f, j_f, nil)
			m[val.String()] = true
		}
	}
	fmt.Println(len(m)) // 9183
}
