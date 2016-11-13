class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        # write your code here
        import heapq
        res = []
        if len(buildings) == 0:
            return res

        buildings.sort()
        # create a set of positions
        positions = set()
        for b in buildings:
            positions.add(b[0])
            positions.add(b[1])
        positions = sorted(positions)

        h = []
        i = 0
        start, currHeight, end = 0, 0, 0

        for pos in positions:
            # if heap empty, insert first
            if len(h) == 0:
                currHeight = 0
                while i < len(buildings) and buildings[i][0] == pos:
                    heapq.heappush(h, [-buildings[i][2], buildings[i][1]])
                    currHeight = max(currHeight, buildings[i][2])
                    start = pos
                    i += 1
            # add buildings whose left end are at the left of pos into heap
            while i < len(buildings) and buildings[i][0] <= pos:
                heapq.heappush(h, [-buildings[i][2], buildings[i][1]])
                i += 1
            # remove those whose right end are at the left of pos
            # those are the ones that we have passed
            while len(h) > 0 and h[0][1] < pos:
                heapq.heappop(h)
            newHeight = -h[0][0]

            if newHeight != currHeight:
                res.append([start, pos, currHeight])
                start = pos
                currHeight = newHeight

            # if a max building ends at pos, process and add to result
            endHere = False
            while len(h) > 0 and h[0][1] <= pos:
                popped = heapq.heappop(h)
                endHere = True
            if endHere:
                res.append([start, pos, newHeight])
                start = pos
                if len(h) > 0:
                    currHeight = -h[0][0]
        return self.mergeIntervals(res)

    def mergeIntervals(self, res):
        ans = []
        for i in range(1, len(res)):
            if res[i][0] != res[i - 1][1] or res[i][2] != res[i - 1][2]:
                ans.append(res[i - 1])
            else:
                res[i][0] = res[i - 1][0]
        ans.append(res[-1])
        del res
        return ans
buildings = [[1,3,3],[2,4,4],[5,6,1]]
print Solution().buildingOutline(buildings)
