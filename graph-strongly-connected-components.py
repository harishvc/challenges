#Find the Strongly Connected Components (SSC) of a directed graph

'''
The Strongly Connected Components of a directed graph are subsets of nodes 
such that each node within a subset can be reached from each other node. 

REFERENCES:
1. http://www.logarithmic.net/pfh/blog/01208083168
2. https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm


TARJAN's ALGORITHM:

Background:
1. Tarjan's algorithm can identify these components efficiently
2. Complexity: The Tarjan algorithm is called once for each node. The algorithm's 
   running time is therefore linear in the number of edges and nodes in G, i.e. O(|V|+|E|).
3. The algorithm takes a directed graph as input, and produces a partition of the graph's vertices 
   into the graph's strongly connected components. Each vertex of the graph appears in exactly one 
   of the strongly connected components. Any vertex that is not on a directed cycle 
   forms a strongly connected component all by itself.

Working:
1. Each node v is assigned a unique integer v.index, which numbers the nodes consecutively 
   in the order in which they are discovered
2. Each node v also maintains a lowlink value, lowlink represents the smallest index of any node 
   known to be reachable from v, including v itself
3. Nodes are placed on a stack in the order in which they are visited
4. When the DFS visits a node v and its descendants the node is not necessarily popped
   4.1 A node remains on the stack after it has been visited if and only if there exists a path 
      in the input graph from node v to some node earlier on the stack
   4.2 Node v must be left on the stack if v.lowlink < v.index
   4.3 Node v must be removed as the root of a strongly connected component if v.lowlink == v.index

USE CASES:
- Install packages with circular dependencies in the best order you can
- Work out in which order a set of equations must be solved, and which must be solved simultaneously
- In a revision control system, find versions that are strongly connected
- Social Media: Find people with similar interest
'''

def stronglyConnectedComponents(G):
    indexCounter = [0]
    stack = []
    lowLinks = {}
    index = {}
    result = []   
    def strongConnect(node):
        #initial setup
        index[node] = indexCounter[0]
        lowLinks[node] = indexCounter[0]
        indexCounter[0] += 1  #increment
        stack.append(node)
        #find successors
        try:
            successors = G[node]
        except:
            successors = []
        for successor in successors:
            if successor not in lowLinks:
                # Successor not visited
                strongConnect(successor)
                lowLinks[node] = min(lowLinks[node], lowLinks[successor])
            elif successor in stack:
                # the successor in stack and strongly connected component (SCC)
                lowLinks[node] = min(lowLinks[node], index[successor])
        
        # If node is a root node, pop the stack and generate SCC
        if lowLinks[node] == index[node]:
            connectedComponent = []
            while True:
                successor = stack.pop()
                connectedComponent.append(successor)
                if successor == node: 
                    break
            component = tuple(connectedComponent)
            result.append(component)
    
    for node in G:
        if node not in lowLinks:
            strongConnect(node)
    
    return result

graph = {'A': set(['C']),
         'B': set(['A']),
         'C': set(['B']),
         'D': set(['A','C'])}

print(stronglyConnectedComponents(graph))
