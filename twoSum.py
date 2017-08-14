class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dic = {}
        for i in range(len(numbers)):
            if dic.get(numbers[i]) is not None:
                return [dic.get(numbers[i]) + 1, i + 1]
            else:
                dic[target - numbers[i]] = i

        print dic

numbers = [2,7,11,15]
target = 9
print Solution().twoSum(numbers, target)