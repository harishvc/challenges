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
from collections import deque

def TopologicalSortDFS(graph):
    result = deque()   #two sided queue, add and remove from both sides
    vertices = set(graph)
    state = {}
    GRAY = 0
    BLACK = 1
    
    def DFS(vertex):
        #Step 1: Change state of vertex
        state[vertex] = GRAY
        #Step 2: Get all neighbors
        for neighbour in graph.get(vertex,()):
            #Step 3: Check state of neighbor
            neighbour_state = state.get(neighbour,None)
            if neighbour_state == BLACK:
                continue
            elif neighbour_state == GRAY:
                raise ValueError("cycle")
                return
            else:
                #Step 4: Process neighbor
                #remove from set
                vertices.discard(neighbour)
                DFS(neighbour)
        #Step 5: Change status and add to result        
        #dequeue specific! 
        result.extendleft(vertex)
        state[vertex] = BLACK
    
    while vertices:
        DFS(vertices.pop())    
    return result

    
'''
a->b
a->c
a->d
c->d
'''
graph1 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": []
}

print("input >>>" , graph1)
print("sorted order >>>", TopologicalSortDFS(graph1))