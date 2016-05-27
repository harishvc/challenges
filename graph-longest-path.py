#Find longest path in a Directed Acyclic Graph from a source vertex

#http://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
#http://stackoverflow.com/questions/29320556/finding-longest-path-in-a-graph

def DFS(graph,current,visited,cpath):
		npath = [] #new path
		for node in graph[current]:
				if node not in visited:
					visited.append(node)
					tpath = cpath + [node] #tmp path
					npath.append(tpath)    #append to existing path
					#extend current path
					npath.extend(DFS(graph,node,visited,tpath))
		return npath


from collections import defaultdict

edges = [[1, 2],[2,4],[1,11],[4,11],[4,6],[4,7],[6,8],[8,9]]

# Step 1: Convert edges in an undirected graph to adjacency list
graph = defaultdict(list) #dictionary of lists
for (s,t) in edges:
    graph[s].append(t)
    graph[t].append(s)

visited = [1] #add source vertex
path = [1]    #add source vertex
# Step 2: DFS from source vertex
result = DFS(graph,1,visited,path)
print("All path from source vertex >>",result)
# Step 3: Sort all path by #nodes in the path
result.sort(key=len,reverse=True)
print("Longest path >>>", result[0])
