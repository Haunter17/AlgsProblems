class Solution:
	def stringMultiplication(self, s1, s2):
		runningSum = []
		for i in range(len(s2) - 1, -1, -1):
			b, c = 0, 0
			currSum = []
			s2Bit = int(s2[i])
			for j in range(len(s1) -1, -1, -1):
				s1Bit = int(s1[j])
				b = (s1Bit * s2Bit + c) % 10
				c = (s1Bit * s2Bit + c) / 10
				currSum.insert(0, b)
			if c != 0:
				currSum.insert(0, c)
			for k in range(len(s2) - 1 - i):
				currSum.append(0)
			# print 'curr', currSum
			if len(runningSum) == 0:
				runningSum = currSum
			else:
				while len(currSum) > len(runningSum):
					runningSum.insert(0, 0)
				carry = 0
				for index in range(len(currSum) - 1, -1, -1):
					# print runningSum, currSum
					# print index, runningSum[index], currSum[index], carry
					runningBit, currBit = runningSum[index], currSum[index]
					runningSum[index] = (runningBit + currBit + carry) % 10
					carry = (runningBit + currBit + carry) / 10
				if carry != 0:
					runningSum.insert(0, carry)
			# print 'running', runningSum, 'curr', currSum


		return ''.join([str(bit) for bit in runningSum])

s1 = '20999009098'
s2 = '4501'
print Solution().stringMultiplication(s1, s2)