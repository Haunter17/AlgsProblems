from sets import Set

class Solution:
	def minHits(self, graph, start, target):
		visited = Set()
		queue1, queue2 = [start], []
		level = 0
		while len(queue1) > 0 or len(queue2) > 0:
			# process queue1
			print 'queue1', queue1
			while len(queue1) > 0:
				curr = queue1.pop(0)
				if curr == target:
					return level
				if curr not in visited:
					visited.add(curr)
					for neighbor in graph[curr]:
						if neighbor not in visited:
							queue2.append(neighbor)
					if len(queue1) == 0:
						level += 1

			# process queue2
			print 'queue2', queue2
			while len(queue2) > 0:
				curr = queue2.pop(0)
				if curr == target:
					return level
				if curr not in visited:
					visited.add(curr)
					for neighbor in graph[curr]:
						if neighbor not in visited:
							queue1.append(neighbor)
					if len(queue2) == 0:
						level += 1

		return level		

G = {
	'A': Set(['B', 'C', 'D']),
	'B': Set(['E']),
	'C': Set(['B']),
	'D': Set(['F']),
	'E': Set(),
	'F': Set(['E', 'G']),
	'G': Set()
}

print Solution().minHits(G, 'A', 'F')