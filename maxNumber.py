class Solution:
    # @param {int[]} nums1 an integer array of length m with digits 0-9
    # @param {int[]} nums2 an integer array of length n with digits 0-9
    # @param {int} k an integer and k <= m + n
    # @return {int[]} an integer array
    def toInt(self, string):
    	if string == '':
    		return -1
    	else:
    		return int(string)

    def compare(self, string1, string2):
    	if self.toInt(string1) < self.toInt(string2):
    		return -1
    	if self.toInt(string1) > self.toInt(string2):
    		return 1
    	if len(string1) < len(string2):
    		return -1
    	else:
    		return 1
    def maxNumberRec(self, nums1, nums2, k):
        # Write your code here
        if k == 0:
        	return ''
        if len(nums1) == 0 and len(nums2) > 0:
        	use2 = str(nums2[0]) + self.maxNumberRec(nums1, nums2[1:], k - 1)
        	lose2 = self.maxNumberRec(nums1, nums2[1:], k)
        	
        	return sorted([use2, lose2], cmp=self.compare)[-1]
        if len(nums2) == 0 and len(nums1) > 0:
        	use1 = str(nums1[0]) + self.maxNumberRec(nums1[1:], nums2, k - 1)
        	lose1 = self.maxNumberRec(nums1[1:], nums2, k)
        	
        	return sorted([use1, lose1], cmp=self.compare)[-1]
        if len(nums1) == 0 and len(nums2) == 0:
        	return ''

        use1 = str(nums1[0]) + self.maxNumberRec(nums1[1:], nums2, k - 1)
        lose1 = self.maxNumberRec(nums1[1:], nums2, k)
        use2 = str(nums2[0]) + self.maxNumberRec(nums1, nums2[1:], k - 1)
        lose2 = self.maxNumberRec(nums1, nums2[1:], k)

        return sorted([use1, use2, lose1, lose2], cmp=self.compare)[-1]

    def maxNumber(self, nums1, nums2, k):
    	table = [[[None for x in range(k + 1)] for x in range(len(nums2) + 1)] for x in range(len(nums1) + 1)]
    	# base case 1
    	for i in range(len(nums1) + 1):
    		for j in range(len(nums2) + 1):
    			table[i][j][0] = ''

    	i = len(nums1)
    	j = len(nums2)
    	for q in range(1, k + 1):
    		table[i][j][q] = ''

    	# base case 2
    	i = len(nums1)
    	for j in range(len(nums2) - 1, -1, -1):
    		for K in range(1, k + 1):
    			use2 = str(nums2[j]) + table[i][j + 1][K - 1]
    			lose2 = table[i][j + 1][K]
    			table[i][j][K] = sorted([use2, lose2], cmp=self.compare)[-1]#use2 if self.toInt(use2) > self.toInt(lose2) else lose2

    	# base case 3
		j = len(nums2)
    	for i in range(len(nums1) - 1, -1, -1):
    		for K in range(1, k + 1):
    			use1 = str(nums1[i]) + table[i + 1][j][K - 1]
    			lose1 = table[i + 1][j][K]
    			table[i][j][K] = sorted([use1, lose1], cmp=self.compare)[-1]

    	for i in range(len(nums1) - 1, -1, -1):
    		for j in range(len(nums2) - 1, -1, -1):
    			for q in range(1, k + 1):
    				use1 = str(nums1[i]) + table[i + 1][j][q - 1]
    				lose1 = table[i + 1][j][q]
    				use2 = str(nums2[j]) + table[i][j + 1][q - 1]
    				lose2 = table[i][j + 1][q]

    				array = sorted([use1, use2, lose1, lose2], cmp=self.compare)
    				table[i][j][q] = array[-1]

    	print table
    	return [int(x) for x in table[0][0][k]]

nums1 = []
nums2 = [11,13,14,8]
k = 2

soln = Solution()
print soln.maxNumberRec(nums1, nums2, k)