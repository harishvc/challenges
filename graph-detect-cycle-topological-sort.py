'''
Question: Sort the vertex (topological sort) of a DAG using depth first search (DFS)

Directed Acyclic Graphs (DAG) have the following properties
1. Their edges show direction  
2. They don't have cycles

Topological sort is ordering of the vertex in a directed acyclic graph (DAG), 
such that if there is a edge from vertex u to vertex v, 
then v appears after u in the ordering


Algorithm: http://codeforces.com/blog/entry/4907
1. Consider we have three colors, and each vertex should be painted with one of these colors.
2. "White color" means that the vertex hasn't been visited yet. 
3. "Gray" means that we've visited the vertex but haven't visited all vertices in its subtree. 
4. "Black" means we've visited all vertices in subtree and left the vertex. 
5. Initially all vertices are white. 
6. When we visit the vertex, we should paint it gray. 
7. When we leave the vertex we paint it black.
8. While processing 
     - IGNORE vertex painted black (since we have processed)
     - ERROR if vertex is GRAY (cycle!!!)
     - process vertex if WHITE 
'''

#Time complexity: O(v+e)  v=#vertices e=#edges    
#https://gist.github.com/kachayev/5910538


'''
0 = WHITE, not visited
1 = Gray, still visiting
2 = visited
'''
def topologicalSortDFS(graph,current,visited,result,cycle):
    #case 2: visiting
    visited[current] = 1
    #for v in graph.get(current,()):
    for v in graph[current]:
        #case 3: visited
        if (visited[v] == 2):
            continue
        #CYCLE!
        elif (visited[v] == 1):
            #print("CYCLE!")
            cycle[0] = True
            return
        else:
            topologicalSortDFS(graph,v,visited,result,cycle)
    #change status
    visited[current] = 2
    #add to result
    result.append(current)
 

#Adjaceny list
graph = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": ["a"]
}


visited = {v:0 for v in graph}
result = []
cycle = [False]
#nodes in a graph need not be connected
for v in graph:
    #case 1: not visited
    if visited[v] == 0:  #nodes not see before
        topologicalSortDFS(graph,v,visited,result,cycle)

if (cycle[0]):
    print("Found cycles!!!")
else:        
    #print("NO CYCLES!!!")
    #Reverse list
    print(result[::-1])