#Given a boolean 2D matrix, find the number of islands.

'''
References
1.http://www.geeksforgeeks.org/find-number-of-islands/
2. http://i.imgur.com/9vxrKNw.png
3. https://www.youtube.com/watch?v=CGMNePwovA0
'''

def isValid(a,row,col,visited,rowmax,colmax):
	if row >= 0 and row <rowmax and col >=0 and col< colmax and a[row][col] == 1 and visited[row][col] == 0:
		return True
	else:
		return False

def DFS(a,row,col,visited,rowmax,colmax):
	#8 neighbours
	#hop factor to go up, down, diagonal
	rowHop = [-1, -1, -1,  0, 0,  1, 1, 1]  
	colHop = [-1,  0,  1, -1, 1, -1, 0, 1]
	for i in range(0,8):
		if isValid(a,row+rowHop[i],col+colHop[i],visited,rowmax,colmax):
			visited[row+rowHop[i]][col+colHop[i]] = 1
			DFS(a,row+rowHop[i],col+colHop[i],visited,rowmax,colmax)

#input map. A group of connected 1s forms an island
a = [[1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1]]
rowmax = 5
colmax = 5
visited = [[ 0 for i in range(colmax)] for y in range(rowmax)]
islands = 0
for row in range(rowmax):
	for col in range(colmax):
		if a[row][col] == 1 and visited[row][col] ==0:
			islands +=1
			visited[row][col] =  1
			DFS(a,row,col,visited,rowmax,colmax)
print("#islands =",islands)
