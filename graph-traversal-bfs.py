'''
Use BFS find all path between two edges.

REFERENCE:
1. http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
2. https://www.cs.berkeley.edu/~vazirani/algorithms/chap4.pdf

NOTES:
1. Breadth-first search visits vertices in increasing order 
   of their distance from the starting point. 
2. Breadth-first search always provides the shortest path between
   two connected vertices   
3. Breadth-first search is a broader, shallower search, rather like the 
   propagation of a wave upon water.
4. Queue is used for implementation
'''

'''
Time complexity is O(|V|) where |V| is the number of nodes, you need to traverse all nodes. 
Space complexity is O(|V|) since at worst case you need to hold all nodes in the queue.
'''

import queue
def BFT(graph,start,end):
	q = queue.Queue()
	#Store node and path
	q.put([start,start])
	#Keep track of visited nodes
	visited = []
	while not q.empty():
		#get node and path from the queue
		nextNode,path = q.get()
		#Found path!
		if nextNode == end:
			yield path
		else:
			#Visit all the edges of nextNone
			visited.append(nextNode)
			for node in graph[nextNode]:
				#node has been visited?
				if node not in visited:
					#Store node and path
					q.put([node,path+node])


#Adjacency list
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

start = 'A'
end  = 'F'
for path in BFT(graph,start,end):
	print("->".join(path))
