class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    memo = {}
    def isMatch(self, s, p):
        # write your code here
    	return self.isMatchHelper(s, p, len(s), len(p))

    def isMatchHelper(self, s, p, m, n):
    	# m: pointer of position in s
    	# n: pointer of position in p
    	key = (m, n)
    	if key in self.memo:
    		return self.memo[key]
        if n == 0:
        	return m == 0
        if m == 0:
        	if n % 2 == 1:
        		return False
        	for i in range(1,n,2):
        		if p[i] != '*':
        			return False
        	return True
        if p[n - 1] != '*' and p[n - 1] != '.':
        	if p[n - 1] != s[m - 1]:
        		return False
        	self.memo[key] = self.isMatchHelper(s, p, m - 1, n - 1)
        	return self.memo[key]
        	# return self.isMatchHelper(s, p, m - 1, n - 1)
        if p[n - 1] == '.':
        	self.memo[key] = self.isMatchHelper(s, p, m - 1, n - 1)
        	return self.memo[key]
        if p[n - 1] == '*':
        	# matches with 0 preceding char:
        	opt1 = self.isMatchHelper(s, p, m, max(0,n - 2))
        	# if opt1:
        	# 	return True
        	# matches with 1 preceding char:
        	opt2 = False
        	if n > 1 and (p[n - 2] == s[m - 1] or p[n - 2] == '.'):
        		opt2 = self.isMatchHelper(s, p, m - 1, n - 1)
        	# if opt2:
        	# 	return True

        	# matches with multi chars:
        	opt3 = False
        	if n > 1 and (p[n - 2] == s[m - 1] or p[n - 2] == '.'):
        		opt3 = self.isMatchHelper(s, p, m - 1, n)

        	self.memo[key] = opt1 or opt2 or opt3
        	return self.memo[key]

# print Solution().isMatch("aab", "c*a*b")
print Solution().isMatch("b", "bc*")
