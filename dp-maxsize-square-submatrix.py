#Given a binary matrix, find out the maximum square size sub-matrix with 1's.

'''
REFERENCE:
1. http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
2. https://prismoskills.appspot.com/lessons/Dynamic_Programming/Chapter_12_-_Maximum_submatrix.jsp

OBSERVATION:
1. Each index position is a square sub-matrix of size 1 (when value = 1)
2. "square sub-matrix" makes the size calculation less complex since we don't have to work with different variations
   - Each index can have maximum of only 1 square sub-matrix

DP TECHNIQUE:
1. If we store the size of the biggest sub-matrix ending at every index in the matrix, 
   then addition of row or a column (at k+1 position) can calculated using the values calculated before 
2. At index position 0,0 if value is 1 then the max size of sub-matrix = 1
3. At index position 0,1 if value is 1 then the max size of sub-matrix = 1 (since square)
4. At index position 1,0 if value is 1 (and 1 & 2) then the max size of sub-matrix = 1 (since square)
5. At index position 1,1 if value is 1 (and 1 & 2) then the max size of sub-matrix = 2 (min of neighbours + 1)
6. If there are 3 square matrix at positions [k-1][j-1],[k-1][j],[k][j-1] with same size then the size at [k][j] = neighbour size + 1
7. If there are 3 square matrix at positions [k-1][j-1],[k-1][j],[k][j-1] with different size then the size at [k][j] = smallest neighbour size + 1
   - add +1 to the size since at each index position the is a square sub-matrix of size 1
'''

def MaxSize(matrix,rows,cols):
	table = [[0 for j in range(cols)] for i in range(rows)]
	size = 0 #max size
	for i in range(1,rows):
		for j in range(1,cols):
			#Important i-1 j-1
			if matrix[i-1][j-1] == 0:
					table[i][j] = 0
			else: 
				#DP Formula!!!
				table[i][j] = 1 + min(table[i-1][j],table[i][j-1],table[i-1][j-1])
				if table[i][j] > size:
					size = table[i][j]
	return size

rows = 3
cols = 5
matrix = [[0 for j in range(cols)] for i in range(rows)]
matrix[0] = [0,1,1,1,1]
matrix[1] = [1,1,1,1,0]
matrix[2] = [0,1,1,1,0]
print("Input Matrix >>")
for i in range(rows):
	for j in range(cols):
		print(matrix[i][j], end=" ")
	print("")

print("Max size of square sub-matrix=",MaxSize(matrix,rows+1,cols+1))