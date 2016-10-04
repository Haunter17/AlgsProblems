from sets import Set

graph = {'A': Set(['B', 'C']),
         'B': Set(['A', 'D', 'E']),
         'C': Set(['A', 'F']),
         'D': Set(['B']),
         'E': Set(['B', 'F']),
         'F': Set(['C', 'E'])}

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

print dfsStack(graph, 'D')
print bfs(graph, 'D')
