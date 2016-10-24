class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range(len(A) - 1, -1, -1):
        	self.siftDown(i, A)

    def siftDown(self, i, A):
        while i < len(A):
        	minimumIndex = i
        	left = i * 2 + 1
        	right = i * 2 + 2
        	if left < len(A) and A[left] < A[minimumIndex]:
        		minimumIndex = left
        	if right < len(A) and A[right] < A[minimumIndex]:
        		minimumIndex = right
        	if minimumIndex == i:
        		break

        	tmp = A[i]
        	A[i] = A[minimumIndex]
        	A[minimumIndex] = tmp

        	i = minimumIndex



A = [3,2,1,4,5]
soln = Solution()
soln.heapify(A)
print A