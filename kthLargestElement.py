class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if len(A) == 0:
            return None
        # partition
        pivot = A[0]
        i, j = 1, len(A) - 1
        while i <= j:
            while j >= 0 and A[j] < pivot:
                j -= 1
            while i < len(A) and A[i] > pivot:
                i += 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        A[0], A[j] = A[j], A[0]
        # print A, j, k
        if j == k - 1:
            return A[j]
        elif j < k - 1:
            return self.kthLargestElement(k - j - 1, A[j + 1:])
        else:
            return self.kthLargestElement(k, A[:j])

A = [9,3,2,4,8]
print Solution().kthLargestElement(3, A)