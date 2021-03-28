package main

import (
	"fmt"
)

func main() {
	var to_add int = 1
	var rolling_sum int = 0
	for i := 1; i <= 500; i++ {
		for j := 1; j <= 4; j++ {
			to_add = to_add + i*2
			rolling_sum += to_add
		}
	}
	fmt.Println(rolling_sum + 1) // 669171001
	// Just a shortcut based on the addition patterns.
}
