def binarySearch(array, target):
	i = 0
	j = len(array) - 1
	while i <= j:
		mid = (i + j) / 2
		if target == array[mid]:
			return mid
		elif target < array[mid]:
			j = mid - 1
		else:
			i = mid + 1
	return -1

def partition(array, k):
	assert(k >= 0 and k < len(array))

	pivot = array[k]
	array[k] = array[0]
	array[0] = pivot

	i, j = 1, len(array) - 1
	while i <= j:
		assert (i >= 0 and i < len(array) and j >= 0 and j < len(array))
		while j >= 0 and array[j] > pivot:
			j -= 1
		while i < len(array) and array[i] < pivot:
			i += 1
		if i < j:
			tmp = array[j]
			array[j] = array[i]
			array[i] = tmp
		# print array

	array[0] = array[j]
	array[j] = pivot
	return array

array = [7,8,2,6,4,3,9]
print partition(array, 6)
