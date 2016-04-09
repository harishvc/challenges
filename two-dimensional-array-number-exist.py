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

#Solution 1: start fro top right and start eliminating rows and cols
def Search(Matrix,input):
    x,y = 0,cols-1  #Top right corner
    while (x >=0 and y >=0 and x < rows and y < cols):
        if ( input > Matrix[x][y]):
            #next row
            x += 1
        elif( input < Matrix[x][y]):
            #next col
            y -= 1
        elif(input == Matrix[x][y]):
            return True
    return False

#solution 2: Modified BST
#convert index to matrix coordinates
def index2Value(matrix,middle):
	cols = len(matrix[0])
	return matrix[middle//cols][(middle%cols)]

#Modified BST
def Search2(matrix,target,start,end):
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

print("Is %d there? %s" % (10,Search(Matrix,10)))
print("Is %d there? %s" % (50,Search(Matrix,50)))
