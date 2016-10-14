#graph = {'A': set(['B', 'C']),
#         'B': set(['A', 'D', 'E']),
#         'C': set(['A', 'F']),
#         'D': set(['B']),
#         'E': set(['B', 'F']),
#         'F': set(['C', 'E'])}
import copy
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
	def findCycle(self, graph, start, maxDegree=3, result=[]):
		print ('graph', graph)
		visited = set()
		queue = [start]
		degree = 0

		while len(queue) > 0 and degree < maxDegree:
			vertex = queue.pop(0)
			if vertex not in visited:
				visited.add(vertex)
				degree += 1
				if degree == maxDegree and start in graph[vertex]:
					print ('in loop', visited)
					#visitList = [e for e in visited]
					tmp = copy.copy(visited)
					if tmp not in result:
						result.append(tmp)
					visited.remove(vertex)
					degree -= 1
					continue
				for v in graph[vertex]:
					if v not in visited:
						queue.append(v)
				

		return result

soln = Solution()
graph = soln.generateGraph('threeMusketeers.txt')
print(soln.findCycle(graph, 2, 3))