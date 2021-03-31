package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var highest_int int
	for i := 1; i <= 10000; i++ {
		var s string = ""
		for j := 1; j <= 9; j++ {
			s += strconv.Itoa(i * j)
			var rolling_sum int = 0
			for k := 1; k <= 9; k++ {
				if strings.Count(s, strconv.Itoa(k)) == 1 {
					rolling_sum += 1
				} else {
					rolling_sum += 10000
				}
			}
			if rolling_sum == 9 && strings.Count(s, "0") == 0 {
				y, e := strconv.Atoi(s)
				_ = e
				if y > highest_int {
					highest_int = y
				}
			}
		}
	}
	fmt.Println(highest_int) // 932718654
	// Stole a lot of the logic from Problem 32.
}
