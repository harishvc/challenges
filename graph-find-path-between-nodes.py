'''
Question: Find the path between two nodes in a DAG 

Algorithm: http://codeforces.com/blog/entry/4907
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

#Time complexity: O(v+e)  v=#vertices e=#edges    
#https://gist.github.com/kachayev/5910538

def FindPath(graph,n1,n2,result):
    state = {}
    GRAY = 0
    BLACK = 1
    status = False
    
    def DFSModified(vertex,result):
        nonlocal status
        state[vertex] = GRAY
        for neighbour in graph.get(vertex,()):
            #print("checking ", vertex , "->", neighbour)
            if (neighbour == n2):
                status = True
                return status
            neighbour_state = state.get(neighbour,None)
            if neighbour_state == BLACK:
                continue
            elif neighbour_state == GRAY:
                raise ValueError("cycle")
                #return False
            else:
                DFSModified(neighbour,result)
                #Check status before starting loop again
                if (status == True):
                    result.append(neighbour)  
                    return status
                state[neighbour] = BLACK
        return status

    return(DFSModified(n1,result))

    
graph1 = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": []
}


n1 = 'a'
n2 = 'e'
result = []
FindPath(graph1,n1,n2,result)
#reverse
result.reverse()
#insert n1 to front
result.insert(0,n1)
#insert n2 to end
result.append(n2)
print("Path between nodes %s and %s: " %(n1,n2))
print('->'.join(result))