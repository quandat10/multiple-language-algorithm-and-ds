package main

import (
	"algorithm/sort"
	"fmt"
)

func main() {
	arr := []int{8, 2, 5, 7, 3, 1, 16, 9}
	fmt.Print("=============Bubble Sort==============\n")
	bubbleSort := sortpa.BubbleSort(arr)
	fmt.Println(bubbleSort)

	fmt.Print("=============Selection Sort==============\n")
	selectionSort := sortpa.SelectionSort(arr)
	fmt.Println(selectionSort)

	fmt.Print("=============Insertion Sort==============\n")
	insertionSort := sortpa.InsertionSort(arr)
	fmt.Println(insertionSort)
}
