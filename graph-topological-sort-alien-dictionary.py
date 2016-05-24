
#Question: Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

'''
REFERENCE:
http://www.elvisyu.com/alien-language-find-order-of-characters/#more-884

ALGORITHM:
Do following for every pair of adjacent words in given sorted array.
a) Let the current pair of words be word1 and word2. One by one compare characters of both words and find the first mismatching characters.
b) Create an edge in g from mismatching character of word1 to that of word2.
'''
def BuildAdjacencyList(a):
	graph = {}
	#create nodes
	for word in a:
		for c in word:
			if c not in graph.keys():
				graph[c] = []
	#create edges
	size = len(graph)
	for i in range(0,size):
		w1 = a[i][0]
		if (i+1 < size):
			w2 = a[i+1][0]
		else:
			w2 = ""
		if (w1 != w2 and len(w2)> 0):
			graph[w1].append(w2)
	#for key in graph:
	#	print(key,graph[key])
	return graph


#Kahn’s algorithm
#https://algocoding.wordpress.com/2015/04/05/topological-sorting-python/
def TopologicalSort(graph):
    TopologicalSortedList = []  #result
    ZeroInDegreeVertexList = [] #node with 0 in-degree/inbound neighbours
    inDegree = { u : 0 for u in graph } #inDegree/inbound neighbours

    #Step 1: Iterate graph and build in-degree for each node
    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    #Step 2: Find node(s) with 0 in-degree
    for k in inDegree:
        #print("##########", k,inDegree[k])
        if (inDegree[k] == 0):
            ZeroInDegreeVertexList.append(k)           

    #Step 3: Process nodes with in-degree = 0
    while ZeroInDegreeVertexList:
        v = ZeroInDegreeVertexList.pop(0) #order in important!
        TopologicalSortedList.append(v)
        #Step 4: Update in-degree
        for neighbour in graph[v]:
            inDegree[neighbour] -= 1
            if (inDegree[neighbour] == 0):
                ZeroInDegreeVertexList.append(neighbour)

    return TopologicalSortedList


a = ["baa", "abcd", "abca", "cab", "cad"]
graph = BuildAdjacencyList(a)
result = TopologicalSort(graph)
print("Topological sort >>> ", "".join(result))