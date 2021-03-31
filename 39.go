package main

import (
	"fmt"
	"sort"
)

func main() {
	var m = make(map[[3]int]bool)
	for i := 1; i <= 998; i++ {
		for j := 1; j <= 998; j++ {
			for k := 1; k <= 998; k++ {
				if i+j+k <= 1000 {
					if i*i+j*j == k*k {
						arr1 := [3]int{i, j, k}
						sort.Ints(arr1[:])
						m[arr1] = true
					}
				}
			}
		}
	}
	var m2 = make(map[int]int)
	for k, v := range m {
		_ = v
		var rolling_sum int
		for j := range k {
			rolling_sum += k[j]
		}
		m2[rolling_sum]++
	}
	var max_k int
	var max_v int
	for k, v := range m2 {
		if v > max_v {
			max_v = v
			max_k = k
		}
	}

	fmt.Println(max_k) // 840
}
