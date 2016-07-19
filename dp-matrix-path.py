#Find #path from top left to bottom right in a 2D binary matrix.
#cell value 1 indicates that you can move through that cell and 0 indicates that you cannot.

#Solution 1: Recursive
#Time complexity: O(2^r+c)
#Each path has r+c cells
#At each cell  there are 2 options
def totalpath1(a,x,y,rowmax,colmax):
	#case 1: outside matrix
	if x == rowmax or y == colmax:
		return 0
	#case 2: not 1
	elif a[x][y] == 0:
		return 0
	#case 3: Reached destination
	elif x == rowmax-1 and y==colmax-1:
		return 1
	#case 4: go down and right
	else:
		#TODO: Add memoization to improve complexity!!!
		t = totalpath1(a,x+1,y,rowmax,colmax) + totalpath1(a,x,y+1,rowmax,colmax)
		#print("%d,%d=%d" % (x,y,t))
		return t

'''
OBSERVATION:
Following the recursive path
1. Cells (value == 1) at the edges have 1 path
2. Cell (value == 1) that have both bottom and right cells determine the #paths
3. If we ignore that last row and last col and go bottom up
4. #path possible at each cell =  #path from cell below + #path from cell on the right 
'''			

#DP solution
def totalpath2(a):
	rowmax = len(a)
	colmax = len(a[0])
	table = [[ 0 for i in range(colmax)] for j in range(rowmax)]

	#copy the table
	for i in range(0,rowmax):
		for j in range(0,colmax):
			if a[i][j] == 1:
				table[i][j] = 1

	for i in range(rowmax-2,-1,-1):
		for j in range(colmax-2,-1,-1):
			if a[i][j] == 1:
					#print("%d,%d" % (i,j))					
					table[i][j] = table[i+1][j] + table[i][j+1]  
	
	#print(table)

	return table[0][0] 


a = [[1,1,0,1],
     [0,1,1,1],
     [0,1,1,1]]

rowmax = len(a)
colmax = len(a[0])

#print(totalpath1(a,0,0,rowmax,colmax))

print("Total #paths=%d" % (totalpath2(a)))

