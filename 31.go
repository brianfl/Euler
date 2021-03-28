package main

import (
	"fmt"
)

func main() {
	rolling_sum := 1
	for a := 0; a <= 200; a++ {
		for b := 0; b <= 100; b++ {
			for c := 0; c <= 40; c++ {
				for d := 0; d <= 20; d++ {
					for e := 0; e <= 10; e++ {
						for f := 0; f <= 4; f++ {
							for g := 0; g <= 2; g++ {
								value := a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100
								if value == 200 {
									rolling_sum++
								}
							}
						}
					}
				}
			}
		}
	}
	fmt.Println(rolling_sum) // 73682
}
