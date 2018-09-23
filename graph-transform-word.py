'''
Convert string a to b using a dictionary of words  #WordLadder

NOTES:
1. Create a adjacency list
2. BFS traversal will find the shortest path

>>> ord('a')
97
>>> ord('z')
122
>>> chr(97)
'a'
'''


# Time Complexity: O(l*(w^2))
# w = # words in the dictionary
# l = sum of length of words in dictionary
#
#
# Space complexity: O(w + e)
# w = # words in the dictionary
# e = sum of edges
def generateAdjacencyList(dictionary):
	graph = {}
	az= [chr(index) for index in range(ord('a'),ord('z')+1)]
	for word in dictionary:
		size = len(word)
		graph[word] = set()
		
		#remove 1 character
		#cat => at , ct , at
		#bat => at, bt, ba
		for index in range(0,size):
			if word[:index]+word[index+1:] in dictionary:
				graph[word].add(word[:index]+word[index+1:])

		#replace 1 character
		#cat => aat, bat ........ zat
		#    => cat, cbt  ........czt
		#
		#bat => aat, bat ......... zat
		# 
		for index in range(0,size):
			for c in az:
				if word[:index]+c+word[index+1:] in dictionary:
					graph[word].add(word[:index]+c+word[index+1:])		

		#add 1 character
		#cat => acat, bcat ....... zcat
		#    =>	caat, cbat ........czat
		for index in range(0,size):
			for c in az:
				if c+word[:index+1]+word[index:] in dictionary:
					graph[word].add(c+word[:index+1]+word[index:])
	return graph


from graph-traversal-bfs import BFT

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
#pre-processing
graph = generateAdjacencyList(dictionary)
start= "bat"
end = "had"
print("Transforming %s to %s >> %s" % (start,end,BFSTraversal(graph,start,end)))

BFT(graph,start,end)