package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	m := make(map[int]bool)
	for i := 1; i <= 10000; i++ {
		for j := 1; j <= 10000; j++ {
			var s string = strconv.Itoa(i*j) + strconv.Itoa(i) + strconv.Itoa(j)
			var rolling_sum int = 0
			for k := 1; k <= 9; k++ {
				if strings.Count(s, strconv.Itoa(k)) == 1 {
					rolling_sum += 1
				} else {
					rolling_sum += 10000
				}
			}
			if rolling_sum == 9 && strings.Count(s, "0") == 0 {
				m[i*j] = true
			}
		}
	}
	var rolling_sum int = 0
	for k, v := range m {
		rolling_sum += k
		_ = v
	}
	fmt.Println(rolling_sum) // 45228
	// An ugly and slow program.
}
