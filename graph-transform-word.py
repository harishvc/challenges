'''
Convert string a to b using a dictionary of words

NOTES:
1. Create a adjacency list
2. BFS traversal will find the shortest path

PYTHON3
#characters a-z
s = list(map(chr,range(ord('a'),ord('z')+1)))
'''

#Time Complexity: O(nm^2). 
#n = # words, 
#m = length of word in dictionary - Pre-processing 
def generateAdjacencyList(dictionary):
	graph = {}
	az = list(map(chr,range(ord('a'),ord('z')+1)))
	for word in dictionary:
		graph[word] = set()
		for i in range(len(word)):
			#Remove 1 character
			if word[:i]+word[i+1:] in dictionary:
				graph[word].add(word[:i]+word[i+1:])
			#Replace 1 chanacter
			for c in az:
				if word[:i]+c+word[i+1:] in dictionary:
					graph[word].add(word[:i]+c+word[i+1:])
			#Add 1 character
			for c in az:
				if word[:i+1]+c+word[i+1:] in dictionary:
					graph[word].add(word[:i+1]+c+word[i+1:])
	#for key in graph:
	#	print(key, graph[key])
	return graph

import queue
def BFSTraversal(graph,start,end):
	visited = set()
	q = queue.Queue()
	#Add current node and path
	q.put([start,start+" "])
	while not q.empty():
		node,path = q.get()
		#important!
		visited.add(node)
		if node == end:
			return path
			break
		else:
			for i in graph[node]-visited:
					q.put([i,path+i+" "])
	return None

dictionary = ["cat", "bat", "hat", "bad", "had"]
graph = generateAdjacencyList(dictionary)
start= "bat"
end = "had"
print("Transforming %s to %s >> %s" % (start,end,BFSTraversal(graph,start,end)))
