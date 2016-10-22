import copy
class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        # write your code here
        # return self.opt(0,nums)
      	N = len(nums)
      	if N == 0:
      		return 0
      	if N == 1:
      		return nums[0]

        table1 = [0 for x in range(N + 1)]
        table2 = [0 for x in range(N)]

        table2[N - 2] = nums[N - 2]
        for index in range(N - 3, -1, -1):
        	loseIt = table2[index + 1]
        	useIt = nums[index] + table2[index + 2]
        	table2[index] = max(loseIt, useIt)

        table1[N - 1] = nums[N - 1]
        for index in range(N - 2, -1, -1):
        	loseIt = table1[index + 1]
        	useIt = nums[index] + table1[index + 2]
        	if index == 0:
        		useIt = nums[index] + table2[index + 2]
        	table1[index] = max(useIt, loseIt)

        return table1[0]

    def opt(self, k, nums):
    	if k >= len(nums):
    		return 0
    	if k == len(nums	) - 1:
    		return nums[k]
    	loseIt = self.opt(k + 1, nums)
    	useIt = 0
    	if k == 0:
    		nums2 = copy.deepcopy(nums[:len(nums) - 1])
    		useIt = nums[0] + self.opt(2, nums2)
    	else:
    		useIt = nums[k] + self.opt(k + 2, nums)
    	return max(loseIt, useIt)

soln = Solution()
nums = [3,6,4]
print soln.houseRobber2(nums)