#Find #rectangles in a binary 2D matrix. All rectangles have value 1 and there are no overlapping rectangles

'''
NOTES
Find the first occurance of 0 you have NOT yet visited
	 - increment count
     - go right all the way to find the top end
     - go row by row to find the bottom end
     - tag coordinate as visited (list with default 'F')
       - convert x,y coordinates into unique id

'''

#convert x,y coordinates into unique id
def getIndex(i,j,cols):
	#IMPORTANT
	return (i*cols) + (j+1)  #+1 since starting with index 0

#given start coordinates find the end of the rectangle and mark all the coordinates as visited
def markVisited(x,y,rows,cols,visited,image):
	#IMPORTANT: store initial y value
	#1:go right
	colstart = y
	while y < cols and image[x][y] ==0:
		y += 1
	#IMPORTANT: decrement y ,earlier while loop
	#2:go down
	y -= 1
	while x < rows and image[x][y] == 0:
		for z in range(colstart,y+1):
			visited[getIndex(x,z,cols)]='T'
		x += 1 	
	

def countRectangles(image):
	rows = len(image)
	cols = len(image[0])
	#Initialize a list with default 'F'
	visited = ['F'] * (rows*cols)
	count = 0
	for i in range(rows):
		for j in range(cols):
			#found new rectangle!
			if image[i][j] == 0 and visited[getIndex(i,j,cols)] == 'F': 
				visited[getIndex(i,j,cols)] = 'T'
				count += 1
				markVisited(i,j,rows,cols,visited,image)
	return count



image = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

print("#rectangles found=%d" % (countRectangles(image)))