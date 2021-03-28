package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	rolling_sum := 0
	for a := 0; a <= 9; a++ {
		for b := 0; b <= 9; b++ {
			for c := 0; c <= 9; c++ {
				for d := 0; d <= 9; d++ {
					for e := 0; e <= 9; e++ {
						for f := 0; f <= 9; f++ {
							for g := 0; g <= 9; g++ {
								var s string = strconv.Itoa(a) + strconv.Itoa(b) + strconv.Itoa(c) + strconv.Itoa(d) + strconv.Itoa(e) + strconv.Itoa(f) + strconv.Itoa(g)
								s_int, x := strconv.Atoi(s)
								if x == nil {
									if float64(s_int) == math.Pow(float64(a), 5.0)+math.Pow(float64(b), 5.0)+math.Pow(float64(c), 5.0)+math.Pow(float64(d), 5.0)+math.Pow(float64(e), 5.0)+math.Pow(float64(f), 5.0)+math.Pow(float64(g), 5.0) {
										rolling_sum += s_int
									}
								}
							}
						}
					}
				}
			}
		}
	}
	fmt.Println(rolling_sum - 1) // 443839
}
