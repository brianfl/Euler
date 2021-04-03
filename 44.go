package main

import (
	"fmt"
	"math"
)

func main() {
	slice_pents := make([]int, 10001)
	map_pents := make(map[int]bool)
	for i := 0; i <= 10000; i++ {
		slice_pents[i] = ((i + 1) * (3*(i+1) - 1)) / 2
		map_pents[slice_pents[i]] = true
	}
	for i := 0; i <= len(slice_pents)-1; i++ {
		map_pents[slice_pents[i]] = true
	}
	var lowest_diff int = 1000000 * 20
	for j := 0; j <= 9999; j++ {
		for k := 0; k <= 9999; k++ {
			if j != k {
				var sum int = slice_pents[j] + slice_pents[k]
				var diff int = int(math.Abs(float64(slice_pents[j] - slice_pents[k])))

				if map_pents[sum] == true && map_pents[diff] == true {
					if diff < lowest_diff {
						lowest_diff = diff
					}
				}
			}

		}
	}
	fmt.Println(lowest_diff) // 5482660
}
