package sortpa

func SelectionSort(arr []int) []int {
	for i := 0; i < len(arr)-1; i++ {
		max := i
		for j := i + 1; j < len(arr); j++ {
			if arr[max] > arr[j] {
				max = j
			}
		}
		arr[i], arr[max] = arr[max], arr[i]
	}
	return arr
}
