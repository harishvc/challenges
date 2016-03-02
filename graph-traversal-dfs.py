'''
Using DFS find all path between two edges.
'''
#Latency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfsPath(graph,start,finish,path=None):
	if path is None:
		path = [start]
	if (start == finish):
		yield path
	#values are unordered in a set
	#store in list and compare convert to set	
	for next in graph[start] - set(path):
		yield from dfsPath(graph,next,finish,path+[next])

#All paths
start = "A"
finish = "F"
print("All paths between %s & %s = %s" % (start,finish,list(dfsPath(graph,start,finish))))
#Shortest path
t =  list(dfsPath(graph,start,finish))
t.sort(key=len)
print("Shortest path=",t[0])
