import copy
import math

class Solution:
	def generateGraph(self, path):
		f = open(path, 'r')
		firstLine = [int(i) for i in f.readline().split()]
		peopleNum, matchesNum = firstLine[0], firstLine[1]
		graph = {}
		for i in range(1, peopleNum + 1):
			graph[i] = set()
		for lineCount in range(matchesNum):
			line = [int(x) for x in f.readline().split()]
			graph[line[0]].add(line[1])
			graph[line[1]].add(line[0])
		return graph

	def findMusketeers(self, graph, start, degree=3, result=[]):
		visited = set()
		queue = [start]

		while len(queue) > 0:
			vertex = queue.pop(0)
			visited.add(vertex)
			curr = copy.deepcopy(visited)
			# remove item in the current path that are not connected with v
			# since in a cycle of 3 every pair of vertices are connected
			for item in visited:
				if item not in graph[vertex] and item != vertex:
					curr.remove(item)
			if len(curr) == degree and start in graph[vertex]:
				if curr not in result:
					curr2 = copy.deepcopy(curr)
					result.append(curr2)
				curr.remove(vertex)
				continue
			for neighbor in graph[vertex]:
				if neighbor not in visited:
					queue.append(neighbor)
		return result

	def findMinRec(self, path):
		graph = self.generateGraph(path)

		# hash table for degree of each vertex
		deg = {}
		for key in graph:
			deg[key] = len(graph[key])

		minRes = math.inf
		for key in graph:
			result = self.findMusketeers(graph, key, degree=3)
			for cycle in result:
				res = sum([deg[key] for key in cycle])
				if res <= minRes:
					minRes = res


		if minRes == math.inf:
			minRes = -1 # no matches
		else:
			minRes -= 6 # subtract mutual recognition
		return minRes


soln = Solution()
print(soln.findMinRec('threeMusketeers.txt'))