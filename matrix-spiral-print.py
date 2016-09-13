#Spiral print matrix

'''
input >>>
    1	2	3	4	5
    6	7	8	9	10
    11	12	13	14	15
    16	17	18	19	20

NOTES:
1. Use 4 pointers to mark start end end of rows and columns
   rowStart = 0
   rowEnd = 4
   colStart = 0
   colEnd = 4
2. Traverse until index pass each other
    - left 2 right
    - top 2 bottom
    - right 2 left
    - bottom 2 top   
'''

def MatrixSpiral(a):
	rowStart = 0
	colStart = 0
	#IMPORTANT: -1
	rowEnd = len(a) -1
	#IMPORTANT: -1
	colEnd =len(a[0]) -1
	#Exit condition: until pointers pass each other! 
	while rowStart <= rowEnd and colStart <= colEnd:
		#left 2 right
		for i in range(colStart,colEnd+1):
			print(a[rowStart][i], end=" ")
		rowStart += 1

		#top to bottom
		for i in range(rowStart,rowEnd+1):
			print(a[i][colEnd], end=" ")
		colEnd -= 1

		#right 2 left
		for i in range(colEnd,colStart-1,-1):
			print(a[rowEnd][i], end=" ")
		rowEnd -=1

		#bottom to top
		for i in range(rowEnd,rowStart-1,-1):
			print(a[i][colStart], end=" ")
		colStart +=1



a = [[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
#Result
#1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12 

MatrixSpiral(a)
print("")
