def solution(S, K):
	sCopy = S.replace('-', '')
	print sCopy
	ans = ''
	for i in range(len(sCopy)):
		ans += sCopy[len(sCopy) - i - 1]
		if i % K == K - 1:
			ans += '-'

	ans = ans[::-1]
	if ans[0] == '-':
		ans = ans[1:]

	realAns = ''
	for x in ans:
		realAns += x.upper()


	return realAns

s1 = '2-4A0R7-4k'
print solution('2-4A0r7-4k', 4)
