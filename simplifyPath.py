class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        # Write your code here
        if len(path) == 0:
        	return ''
        stack = []
        i = 0
        while i < len(path):
        	while i < len(path) and path[i] == '/':
        		i += 1
        	j = i + 1
        	while j < len(path) and path[j] != '/':
        		j += 1
        	curr = path[i: j]
        	if curr != '..' and curr != '.':
        		stack.append(curr)
        	if curr == '..' and len(stack) > 0:
        		stack.pop()
        	i = j + 1

        ans = '/'
        if len(stack) == 0:
        	return ans
        
        for v in stack:
        	ans += v
        	ans += '/'

       	return ans[:len(ans) - 1]

path = '/../home'
print Solution().simplifyPath(path)