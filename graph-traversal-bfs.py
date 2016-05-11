'''
Use BFS find all path between two edges.

REFERENCE:
1. http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
2. https://www.cs.berkeley.edu/~vazirani/algorithms/chap4.pdf

NOTES:
1. Breadth-first search visitS vertices in increasing order 
   of their distance from the starting point. 
2. Breadth-first search always provides the shortest path between
   two connected vertices   
3. Breadth-first search is a broader, shallower search, rather like the 
   propagation of a wave upon water.
4. Queue is used for implementation
'''

#Latency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

import queue
def graphPathBFS(graph,start,end):
	q = queue.Queue()
	visited = set()
	#current node and path added to queue
	q.put([start,start])
	while not q.empty():
		next,path = q.get()
		if next == end:
				yield path
		else:
			visited.add(next)
			for node in graph[next] - visited:
				#place node and path in the queue
				q.put([node,path+node])

start = "A"
end="F"
paths = graphPathBFS(graph,start,end)
print("All path between %s & %s (BFS)" % (start,end))
for path in paths:
	print("->".join(path))
#Shortest path
t =  list(graphPathBFS(graph,start,end))
t.sort(key=len)
print("Shortest path=","->".join(t[0]))