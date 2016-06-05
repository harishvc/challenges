'''
Question: Given a two dimensional matrix where rows and columns are sorted in increasing order. 
Design an efficient algorithm that decides whether a number X appears in A.
'''

rows = 5
cols = 5
count = 0 
#Initialize matrix with increasing values
def init():
    global count
    count += 1
    return count


#OBSERVARTION:
#1. At any given index i and j. All values a[0][j] .... a[i-1][j] are less than a[i][j]
#2. At any given index i and j. All values a[i][0] .... a[i][j+1] are greater than a[i][j]
#3. If we start at top right, we can elimainate a row or column (Binary Search technique)

#Solution 1: start from top right and start eliminating rows and cols
#Time complexity: O(m+n) , m=#rows, n=#cols 
def Search(Matrix,target):
	#rows
	rows = len(Matrix)
	#cols
	cols = len(Matrix[0])
	x,y = 0,cols-1  #Top right corner
	while (x < rows and y >=0):
		if ( target > Matrix[x][y]):
			#next row
			x += 1
		elif( target < Matrix[x][y]):
			#next col
			y -= 1
		elif(target == Matrix[x][y]):
			return True
	return False

#solution 2: Modified BST
#convert index to matrix coordinates
def index2Value(matrix,middle):
	cols = len(matrix[0])
	return matrix[middle//cols][(middle%cols)]


def Search2(Matrix,target,start,end):
	print("### start=%d end=%d" %(start,end))
	if start == end and index2Value(matrix,start) == target:
		print("Found")
		return
	elif start == end:
		print("Not Found")
		return
	middle = start + (end-start)//2
	middleValue = index2Value(matrix,middle)
	print("middle=%d middleValue=%d" % (middle,middleValue))
	if middleValue == target:
		print("Found")
		return
	elif middleValue < target: 
		#go right
		return search(matrix,target,middle+1,end)
	else:
		#go left
		return search(matrix,target,start,middle-1)
    
Matrix = [[init() for x in range(cols)] for y in range(rows)]

#Solution 1        
print("Is %d there? %s" % (10,Search(Matrix,10)))
print("Is %d there? %s" % (50,Search(Matrix,50)))

#Solution 2
#rows = len(Matrix)
#cols = len(Matrix[0])
#target = 9
#Search2(Matrix,target,0,rows*cols-1)
