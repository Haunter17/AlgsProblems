class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        return self.lcpHelper(strs, 0)

    def lcpHelper(self, strs, level):
    	if len(strs) == 0:
    		return ''
    	for string in strs:
    		if level >= len(string):
    			return ''

    	prefix = strs[0][level]

    	for string in strs:
    		if string[level] != prefix:
    			return ''
    	return prefix + self.lcpHelper(strs, level + 1)

strs = ['ABCDEFG', 'ABCEFG', 'ABCEFA']
print Solution().longestCommonPrefix([])