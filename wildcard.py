class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        if len(p) == 0:
        	return len(s) == 0
        if len(s) == 0:
        	return p.count('*') == len(p)

        if p[len(p) - 1] == '?':
        	return self.isMatch(s[:len(s) - 1], p[:len(p) - 1])
        if p[len(p) - 1] != '*':
        	if p[len(p) - 1] == s[len(s) - 1]:
        		return self.isMatch(s[:len(s) - 1], p[:len(p) - 1])
        	else:
        		return False
        else:
        	for i in range(len(s) + 1):
        		if self.isMatch(s[:len(s) - i], p[:len(p) - 1]):
        			return True
        	return False

    def isMatchDP(self, s, p):
    	table = [[None for i in range(len(p) + 1)] for j in range(len(s) + 1)]

    	# init
    	table[0][0] = True
    	for row in range(1, len(s) + 1):
    		table[row][0] = False
    	for col in range(1, len(p) + 1):
    		table[0][col] = (p[:col].count('*') == col)

    	for col in range(1, len(p) + 1):
    		for row in range(1, len(s) + 1):
    			if p[col - 1] == '?':
    				table[row][col] = table[row - 1][col - 1]
    			elif p[col - 1] != '*':
    				if p[col - 1] == s[row - 1]:
    					table[row][col] = table[row - 1][col - 1]
    				else:
    					table[row][col] = False
    			else:
    				for i in range(row + 1):
    					if table[row - i][col - 1] == True:
    						table[row][col] = True
    						break
    				if table[row][col] is None:
    					table[row][col] = False

    	print table
    	return table[len(s)][len(p)]



s = 'aab'
p = '*ab'
print Solution().isMatchDP(s, p)        	     
