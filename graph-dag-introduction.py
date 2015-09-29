'''
Question: Implement a directed acyclic graph

Directed Acyclic Graphs (DAG) have the following properties
1. Their edges show direction  
2. They don't have cycles
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
    
G = Graph()
G.addEdge('A', 'B')   
G.addEdge('A', 'C')   
print("#Vertices: ", G.getVerticesCount())
print("All vertices: ", G.getVertices())
print("All edges: ", G.getEdges())