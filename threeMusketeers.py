import copy
import math
#graph = {'A': set(['B', 'C']),
#         'B': set(['A', 'D', 'E']),
#         'C': set(['A', 'F']),
#         'D': set(['B']),
#         'E': set(['B', 'F']),
#         'F': set(['C', 'E'])}
graphB = {1: set([2,4]),
          2: set([1,3]),
		  3: set([2,4]),
		  4: set([1,3])}
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
		#print ('graph', graph)
		visited = set()
		queue = [start]

		while len(queue) > 0:
			#print('h')
			vertex = queue.pop(0)
		#if vertex not in visited:
			visited.add(vertex)
			#if len(visited) == degree and start not in graph[vertex]:
			#	continue
			curr = copy.deepcopy(visited)

			#print(curr, vertex)
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
			minRes = -1
		else:
			minRes -= 6
		return minRes


soln = Solution()
#graph = soln.generateGraph('threeMusketeers.txt')
#print(soln.findMusketeers(graph, 1, degree=3))
print(soln.findMinRec('threeMusketeers.txt'))