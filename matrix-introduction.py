#Introduction to Matrix

from random import randint

# Creates nxm matris
n = 5 #rows
m = 3 #cols
matrix = [[0 for x in range(n)] for x in range(m)]

#Initialize matrix
for row in range(0,len(matrix)):
	for col in range(0,len(matrix[row])):
		matrix[row][col] = randint(1,26)

#Print Matrix 
for row in range(0,len(matrix)):
	for col in range(0,len(matrix[row])):
		print("%d" % (matrix[row][col]),end=" ")
	print("")
	
