def subsetSumZero(arr):
	if 0 in arr:
		return True
	arrPos = [x for x in arr if x > 0]
	arrNeg = [-x for x in arr if x < 0]
	target = min(sum(arrPos), sum(arrNeg))

	posList = subsetSum(arrPos, target)
	negList = subsetSum(arrNeg, target)

	for i in range(1, len(posList)):
		if posList[i] and negList[i]:
			return i
	return -1


def subsetSum(arr, target):
	# if target == 0:
	# 	return True
	# if len(arr) == 0:
	# 	return False
	# it = arr[0]
	# useIt = subsetSum(arr[1:], target - it)
	# loseIt = subsetSum(arr[1:], target)
	# return useIt or loseIt
	table = [[False for x in range(target + 1)] for y in range(len(arr) + 1)]
	for row in range(len(table)):
		table[row][0] = True
	# print table
	for row in range(len(table) - 2, -1, -1):
		for col in range(1, target + 1):
			# print row, col, col - arr[row]
			rem = col - arr[row]
			if rem < 0:
				continue
			useCell = table[row + 1][col - arr[row]]
			loseCell = table[row + 1][col]
			table[row][col] = useCell or loseCell

	return table[0]




arr = [1,-3,4,-5]
target = 0

print subsetSumZero(arr)