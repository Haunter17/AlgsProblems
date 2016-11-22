class Solution:
	def stringMinus(self, s1, s2):
		ans = ''
		negative = False
		if len(s1) < len(s2):
			negative = True
		elif len(s1) == len(s2):
			for i in range(len(s1)):
				if int(s1[i]) > int(s2[i]):
					negative = False
					break
				if int(s1[i]) < int(s2[i]):
					negative = True
					break
		if negative:
			s1, s2 = s2, s1

		carry = 0
		i = 0
		# process the s2 part
		while i < len(s2):
			bit1 = int(s1[-(i + 1)])
			bit2 = int(s2[-(i + 1)])
			currBit = bit1 - bit2 - carry
			carry = 0
			if currBit < 0:
				currBit += 10
				carry = 1
			ans = str(currBit) + ans
			i += 1

		# process the s1 part
		while i < len(s1):
			bit1 = int(s1[- (i + 1)])
			currBit = bit1 - carry
			carry = 0
			if currBit < 0:
				currBit += 10
				carry = 1
			ans = str(currBit) + ans
			i += 1

		# strip beginning zeros
		firstNoneZero = 0
		for j in range(len(ans)):
			if ans[j] != '0':
				firstNoneZero = j
				break

		ans = ans[j:]
		if negative:
			ans = '-' + ans
		return ans

s1 = '10002'
s2 = '33'
print Solution().stringMinus(s1, s2)