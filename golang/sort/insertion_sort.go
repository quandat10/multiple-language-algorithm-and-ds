package sortpa

func InsertionSort(arr []int) []int {
	for i := 0; i < len(arr)-1; i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && key < arr[j] {
			arr[j+1] = arr[j]
			j -= 1
		}
		arr[j+1] = key
	}

	return arr
}
