from sets import Set

graph = {'A': Set(['B', 'C']),
         'B': Set(['A', 'D', 'E']),
         'C': Set(['A', 'F']),
         'D': Set(['B']),
         'E': Set(['B', 'F']),
         'F': Set(['C', 'E'])}

# graph = {'A': {'B', 'C'},
#          'B': {'A', 'D', 'E'},
#          'C': {'A', 'F'},
#          'D': {'B'},
#          'E': {'B', 'F'},
#          'F': {'C', 'E'}}

def dfsRecursive(G, start, visited=None):
	if not visited:
		visited = Set()
	visited.add(start)
	for vertex in G[start]:
		if vertex not in visited:
			dfsRecursive(G, vertex, visited)
	return visited

def dfsStack(graph, start):
    visited, stack = Set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for v in graph[vertex]:
            	if v not in visited:
            		stack.append(v)
    return visited

def bfs(graph, start):
	visited = Set()
	queue = [start]
	while len(queue) > 0:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			for v in graph[vertex]:
				if v not in visited:
					queue.append(v)
	return visited

def bfsCount(graph, start, end):
	visited = set()
	q1, q2 = [], []
	q1.append(start)
	count = 0

	while len(q1) > 0 or len(q2) > 0:
		# process the first queue
		# if visited, just pop
		# else, put all neighbors into the other queue
		while len(q1) > 0:
			curr = q1.pop(0)
			if curr not in visited:
				visited.add(curr)
				if curr == end:
					return count
				for neighbor in graph[curr]:
					q2.append(neighbor)
			if len(q1) == 0:
				count += 1

		while len(q2) > 0:
			curr = q2.pop(0)
			if curr not in visited:
				visited.add(curr)
				if curr == end:
					return count
				for neighbor in graph[curr]:
					q1.append(neighbor)
			if len(q2) == 0:
				count += 1

testGraph = {'1': set(['2', '3']),
			'2': set(['3','5']),
			'3': set(['4']),
			'4': set(['5'])}
print bfsCount(testGraph, '1', '5')

# print dfsStack(graph, 'D')
# print bfs(graph, 'D')
