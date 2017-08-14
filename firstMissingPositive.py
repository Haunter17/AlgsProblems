class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        i = 0
        while i < len(A):
            if A[i] == i + 1:
                i += 1
                continue
            elif A[i] > len(A) or A[i] <= 0:
                i += 1
                continue
            elif A[A[i] - 1] != A[i]:
                tmp = A[i]
                A[i] = A[A[i] - 1]
                A[tmp - 1] = tmp
                # A[i], A[A[i] - 1] = A[A[i] - 1], A[i]
                # print A
                # break
            else:
                i += 1
                # print 'ha'
        
        for i in range(len(A)):
            if i != A[i] - 1:
                return i + 1
        
        return len(A) + 1

arr = [2,1]
print Solution().firstMissingPositive(arr)