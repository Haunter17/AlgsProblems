class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        import heapq
        assert(n > 0)
        assert(len(primes) > 0)
        primes.sort()
        h = []
        ans = (1,0)
        heapq.heappush(h, ans)
        while n > 0:
            ans = heapq.heappop(h)
            for i in range(ans[1], len(primes)):
                heapq.heappush(h, (ans[0] * primes[i], i))
            n -= 1
        return ans[0]

print Solution().nthSuperUglyNumber(6, [2,7, 13, 19])