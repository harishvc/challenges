'''
Use DFS find all path between two edges.

REFERENCE:
1. http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
2. https://www.cs.berkeley.edu/~vazirani/algorithms/chap4.pdf

NOTES:
1. Depth-first search makes deep incursions into a graph, retreating 
   only when it runs out of new nodes to visit. 
2. DFS can end up taking a long and convoluted route to a vertex 
   that is actually very close by.
'''

#Latency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def graphPathDFS(graph,start,end,visited,path):
	if start == end:
		yield path
	elif start not in visited:
		visited.add(start)
		for node in graph[start]:
			yield from graphPathDFS(graph,node,end,visited,path+[node])

start = "A"
end="F"
paths = graphPathDFS(graph,start,end,set(),[start])

print("All path between %s & %s (DFS)" % (start,end))
for path in paths:
	print("->".join(path))
#Shortest path
t =  list(graphPathDFS(graph,start,end,set(),[start]))
t.sort(key=len)
print("Shortest path=","->".join(t[0]))

