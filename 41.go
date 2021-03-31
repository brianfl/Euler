package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	var highest_int int
	for i := 1; i <= 9999999; i++ {
		var s string = strconv.Itoa(i)
		if !(i%5 == 0 || i%2 == 0) {
			var rolling_sum int = 0
			for k := 1; k <= len(s); k++ {
				if strings.Count(s, strconv.Itoa(k)) == 1 {
					rolling_sum += 1
				} else {
					rolling_sum += 10000
				}
			}
			if rolling_sum == len(s) && strings.Count(s, "0") == 0 {
				if isPrime(i) && i > highest_int {
					highest_int = i
				}
			}

		}
	}

	fmt.Println(highest_int) // 7652413
	// Good it wasn't higher, because this program slows down a lot of 8 and 9 digit values.
}

func isPrime(number int) bool {
	var counter int
	f_n := float64(number)
	sq_p := int(math.Pow(f_n, float64(.5)) + 1)

	for i := 2; i <= sq_p; i++ {
		if number%i == 0 {
			counter++
		}
	}
	if counter == 0 {
		return true
	}
	return false
}
