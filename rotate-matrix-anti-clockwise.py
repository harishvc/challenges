#Rotate 2D matrix by 90

#Questions: 
#1. Clockwise or anti clock wise?
#2. Is it a cube?
#3. Can the values be modified?

#http://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

import sys
sys.path.append("../mylib")
import doless

#Rotate 2D matrix by 90 anti clock
def rotateAC90():
	a2 = [[1,2],[3,4]]

	a = [[1,2,3,4],
		   [5,6,7,8],
		   [9,10,11,12],
		   [13,14,15,16]]

	SIZE = len(a[0])
	print("Input Matrix >>>")
	doless.PrintMatrix(a)	

	for i in range(0,SIZE//2):  #SIZE//2 since each cycle covers 2 rows, 2 cols
		for j in range(i,SIZE-i-1):  #SIZE-i-1 since each CYCLE covers 2 cols, 2rows
			#step 1: store index 0,0
			tmp = a[i][j]
			#step 2: move top right to top left
			a[i][j] = a[j][SIZE-i-1]                   #a[0][0] = a[0][1]
			#step 3: move  bottom right to top right
			a[j][SIZE-i-1] =  a[SIZE-1-i][SIZE-1-j]    #a[0][1] = a[1][1]
			#step 4: move bottom left to bottom right
			a[SIZE-1-i][SIZE-1-j] = a[SIZE-1-j][i]     #a[1][1] = a[1][0]
			#step 5: move top left to bottom left
			a[SIZE-1-j][i]  = tmp  				       #a[1][0] = tmp

	print("\nMatrix rotated 90 anti clockwise")
	doless.PrintMatrix(a)	

rotateAC90()

