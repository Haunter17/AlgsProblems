class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        assert(len(numbers) >= 3)
        
        ans = numbers[0] + numbers[1] + numbers[2]
        for i in range(0, len(numbers) - 1):
            head, tail = i + 1, len(numbers) - 1
            while head < tail:
                option = numbers[i] + numbers[head] + numbers[tail]
                if abs(option - target) < abs(ans - target):
                    print i, head, tail
                    ans = option
                elif option > target:
                    tail -= 1
                else:
                    head += 1
        return ans


numbers = [2,7,11,15]
target = 3
print Solution().threeSumClosest(numbers, target)