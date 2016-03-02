'''
Using BFS find all path between two edges & the shortest path 
'''

#Latency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def bfsPath(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0) #IMPORTANT!!!
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfsPath(graph, start, goal))
    except StopIteration:
        return None

start = "A"
finish = "F"
print("All paths between %s & %s = %s" % (start,finish,list(bfsPath(graph,start,finish))))
print("Shortest path=",shortest_path(graph, start, finish)) 
