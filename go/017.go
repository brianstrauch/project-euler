package main

import "fmt"

var (
	ones  = []string{"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	teens = []string{"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
	tens  = []string{"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}
)

func main() {
	// 1 - 9
	to9 := 0
	for i := 1; i < 10; i++ {
		to9 += len(ones[i])
	}

	// 1 - 99
	to99 := to9
	for i := 0; i < 10; i++ {
		to99 += len(teens[i])
	}
	for i := 2; i < 10; i++ {
		to99 += len(tens[i])*10 + to9
	}

	// 1 - 1000
	to1000 := to99
	for i := 1; i < 10; i++ {
		to1000 += (len(ones[i])+len("hundred"))*100 + len("and")*99 + to99
	}
	to1000 += len("one") + len("thousand")

	fmt.Println(to1000)
}
