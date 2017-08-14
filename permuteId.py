class Solution:
	def permuteString(self, string):
		if len(string) == 0:
			return []
		if len(string) == 1:
			return [string]

		coll = []
		string = ''.join(sorted(string))
		# string = sorted(string)
		for i in range(len(string)):
			restString = string[0:i] + string[i + 1:len(string)]
			restPerm = self.permuteString(restString)
			for perm in restPerm:
				perm = string[i] + perm
				# perm.insert(0, string[i])
				coll.append(perm)

		return coll


string = '1v7'
print Solution().permuteString(string)