'''
Questions: 
1. Check if a directed graph is acyclic
2. Sort the vertex (topological sort)

Directed Acyclic Graphs (DAG) have the following properties
1. Their edges show direction  
2. They don't have cycles

Topological sort is ordering of the vertex in a directed acyclic graph (DAG), 
such that if there is a edge from vertex u to vertex v, 
then v appears after u in the ordering
'''

class Vertex:
    def __init__(self,node):
        self.id = node
        self.neighbours = []
        self.inDegree = 0 #number of edges leading to the vertex
    
        
    def addNeighbour(self,neighbour):
        self.neighbours.append(neighbour)
        
    def getNeighbours(self):
        return self.neighbours
    
    def getInDegree(self):
        return self.inDegree

class Graph:
    def __init__(self):
        self.vertexCount = 0
        self.vertexInfo = {}

    #iteration
    def __iter__(self):
        return iter(self.vertexInfo.values())
        
    def addVertex(self,node):
        self.vertexCount += 1
        newVertex = Vertex(node)
        self.vertexInfo[node] = newVertex
        return newVertex
        
    def addEdge(self,frm,to):
        #Add vertex 
        if frm not in self.vertexInfo:
            fromVertex = self.addVertex(frm)
        else:
            fromVertex = self.vertexInfo[frm]
        if to not in self.vertexInfo:
            toVertex = self.addVertex(to)
        else:
            toVertex = self.vertexInfo[to]
        #Add neighbour for frm vertex
        fromVertex.addNeighbour(toVertex)
        #Increment inDegree for to vertex
        toVertex.inDegree += 1
    
    def getVertices(self):
        return self.vertexInfo.keys()
    
    def getVerticesCount(self):
        return self.vertexCount
    
    def getEdges(self):
        edges = []
        for v in self:
            for w in v.getNeighbours():
                edges.append([v.id,w.id])
        return edges
    
#Time complexity: O(v+e)  v=#vertices e=#edges    
def TopologicalSort(G):
    TopologicalSortedList = []  #stored sequence
    ZeroInDegreeVertexList = [] #store all nodes with inDegree = 0
    RemainingInDegree = {}      #store all node with inDegree > 0
    
    #Step 1: Iterate all vertex in the graph and check inDegree
    for v in G:
        inDegree = v.getInDegree()
        if inDegree == 0:
            ZeroInDegreeVertexList.append(v)
        else:
            RemainingInDegree[v] = inDegree

    #Step 2: Process nodes with inDegree = 0
    while len(ZeroInDegreeVertexList):
        node = ZeroInDegreeVertexList.pop(0) #order in important!
        TopologicalSortedList.append(node.id)
        #Step 3: Decrement inDegreee of neighbour nodes
        for neighbour in node.getNeighbours():
            neighbour.inDegree -=1
            if (neighbour.inDegree == 0):
                ZeroInDegreeVertexList.append(neighbour)
    
    nodes  = G.getVertices()
    if len(TopologicalSortedList) == len(nodes):
        #Acyclic
        return (True,TopologicalSortedList)
    else:
        return (False,TopologicalSortedList)
    
G = Graph()
G.addEdge('A', 'B')   
G.addEdge('B', 'C')
#G.addEdge('C', 'A')


print("#Vertices: ", G.getVerticesCount())
print("All vertices: ", G.getVertices())
print("All edges: ", G.getEdges())

status,TopologicalsortedList = TopologicalSort(G)
print("Valid DGA? ", status)
print("sorted list >>> ", TopologicalsortedList)
