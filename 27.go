package main

import (
	"fmt"
	"math"
)

func main() {
	var max_prod float64 = 0
	var max_counter int = 0
	for a := -1000; a <= 1000; a++ {
		for b := -1000; b <= 1000; b++ {
			var tracker int = 0
			var n float64 = 0
			var a_f float64 = float64(a)
			var b_f float64 = float64(b)

			for {
				value := math.Pow(n, 2) + a_f*n + b_f
				if is_prime(value) == true {
					n++
					tracker++
				} else {
					if tracker > max_counter {
						max_counter = tracker
						max_prod = a_f * b_f
					}
					break
				}
			}
		}
	}
	fmt.Println(max_prod) // -59231
}

func is_prime(number float64) bool {
	if number <= 0 {
		return false
	}
	var root_plus int = int(math.Pow(number, .5)) + 1
	var counter int = 0
	for i := 2; i <= root_plus; i++ {
		if int(number)%i == 0 {
			counter++
		}
	}
	if counter == 0 {
		return true
	}
	return false
}
