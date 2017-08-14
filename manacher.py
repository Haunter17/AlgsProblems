def preprocess(s):
	# inserting a reserved char at the beginning
	newS = '@'
	# inserting another reserved char in middle
	for ch in s:
		newS += '#'
		newS += ch
	newS += '#'
	# inserting a third reserved char at the end
	newS += '$'
	return newS

def findLongestPalindrome(s):
	newS = preprocess(s)
	P = [0] * len(newS)
	# current center
	center, right = 0, 0
	for i in range(1, len(newS) - 1):
		mirror = center - (i - center)
		if right > i:
			if P[mirror] < right - i:
				P[i] = P[mirror]
			else:
				P[i] = right - i
			# P[i] = min(right - i, P[mirror])
		# expanding around i
		while newS[i + 1 + P[i]] == newS[i - 1 - P[i]]:
			P[i] += 1

		# update center, right if palindrome centered at i expands
		# past right
		if i + P[i] > right:
			center, right = i, i + P[i]
		# end of core
	maxLength, maxCenter = 0, 0
	for i in range(1, len(P) - 1):
		if P[i] > maxLength:
			maxCenter, maxLength = i, P[i]

	# stripping off reserved chars
	maxPalindrome = newS[maxCenter - maxLength: \
	maxCenter + maxLength + 1].replace('@', '').replace('#', '').replace('$', '')
	return maxPalindrome



test = 'cabbad'
print findLongestPalindrome(test)