'''
Detect cycle in a directed graph using DFS

A cycle is a closed path - we can visit a node for the second time before all its 
decendents have been visited

NOTES:
1. Modify DFS to keep track vertex state. Consider we have three colors, and each vertex should be painted with one of these colors.
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


#source: https://algocoding.wordpress.com/2015/04/02/detecting-cycles-in-a-directed-graph-with-dfs-python/comment-page-1/
def cycle_exists(G):                     # - G is a directed graph
    color = { u : "white" for u in G  }  # - All nodes are initially white
    found_cycle = [False]                # - Define found_cycle as a list so we can change
                                         # its value per reference, see:
                                         # http://stackoverflow.com/questions/11222440/python-variable-reference-assignment
    for u in G:                          # - Visit all nodes.
        if color[u] == "white":
            dfs_visit(G, u, color, found_cycle)
        if found_cycle[0]:
            break
    return found_cycle[0]


def dfs_visit(G, u, color, found_cycle):
    if found_cycle[0]:                          # - Stop dfs if cycle is found.
        return
    color[u] = "gray"                           # - Gray nodes are in the current path
    for v in G[u]:                              # - Check neighbors, where G[u] is the adjacency list of u.
        if color[v] == "gray":                  # - Case where a loop in the current path is present.  
            found_cycle[0] = True       
            return
        if color[v] == "white":                 # - Call dfs_visit recursively.   
            dfs_visit(G, v, color, found_cycle)
    color[u] = "black" 

graph_example_1 = { 0 : [1],
                    1 : [2],
                    2 : [3],
                    3 : [4],
                    4 : [3] }


print("Cycle?", cycle_exists(graph_example_1))    
