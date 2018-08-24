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

'''
Time complexity is O(|V|), #nodes. 
Space complexity in a recursive implementation is O(h) [worst case], where h is the maximal depth of the graph
'''

#Depth First Traversal
def DFT(graph,current,visited,target,path):
	for node in graph[current]:
		if node == target:
			path.append(node)
			yield path
			path.pop()
		elif node not in visited:
			visited.append(node)
			path.append(node)
			yield from DFT(graph,node,visited,target,path)
			path.pop()
			visited.pop()

#Adjacency list
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

start = 'A'
end  = 'F'

for path in DFT(graph,start,[start],end,[start]):
	print("->".join(path))