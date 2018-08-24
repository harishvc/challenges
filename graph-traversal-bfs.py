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
def BFT(graph,traversed_nodes,visited,target):
	while not traversed_nodes.empty():
		current = traversed_nodes.get()
		current_node,current_path = current[0],current[1]
		if current_node == target:
			yield current_path
		elif current_node not in visited:
			visited.append(current_node)
			for node in graph[current_node]:
				traversed_nodes.put([node,current_path+node])	



#Adjacency list
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

start = 'A'
end  = 'F'
q = queue.Queue()
q.put([start,start])
for path in BFT(graph,q,[],end):
	print("->".join(path))

