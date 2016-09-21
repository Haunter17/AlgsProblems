class Solution:
    """docstring for Solution"""
    def backPackVIRec(self, nums, target):
        if target <= 0:
            return 0
        if len(nums) == 0:
            return 0     
        ans = 0
        for i in range(len(nums)):
            if nums[i] == target:
                ans += 1
            else:
                ans += self.backPackVIRec(nums, target - nums[i])
        return ans

    def backPackVI(self, nums, target):
        table = [0 for i in range(target + 1)]
        for i in range(1,len(table)):
            for j in range(len(nums)):
                rem = i - nums[j]
                if rem == 0:
                    table[i] += 1
                elif rem > 0:
                    table[i] += table[rem]
        print table
        return table[-1]

nums = [1, 2, 4]
target = 4

soln = Solution()
print soln.backPackVI(nums, target)
print soln.backPackVIRec(nums, target)