def combinationSum(arr, target):
	res = []
	curr = []
	combinationHelper(arr, target, 0, curr, res)
	return res

def combinationHelper(arr, target, level, curr, res):
	print "curr", curr
	print "target", target
	if target == 0:
		newList = sorted(list(curr))
		# if newList not in res:
		res.append(newList)
		return

	if target < 0:
		return

	for i in range(level, len(arr)):
		currVal = arr[i]
		if currVal <= target:
			curr.append(currVal)
			combinationHelper(arr, target - currVal, i, curr, res)
			curr.pop()
			# print "popped"


arr = [1, 6, 12]
target = 13

print "ans", combinationSum(arr, target)
