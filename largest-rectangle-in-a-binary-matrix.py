#Find largest rectangle containing only zeros in an N×N binary matrix

'''
NOTES/OBSERVATION
1. Build a histogram with heights
2. Find the max area fo each row

Reference
1. http://stackoverflow.com/questions/2478447/find-largest-rectangle-containing-only-zeros-in-an-n%C3%97n-binary-matrix
'''


def Printtable(table,rows,cols):
	for i in range(rows):
		for j in range(cols):
			print(table[i][j], end="  ")
		print("")


import sys
sys.path.append("./")
import Histogram
def BuildHistogram(a,rows,cols):
	#DP Table
	#Populate for each column: longest height based on 0's
	table = [[0 for i in range(cols)] for j in range(rows)]
	for i in range(cols):
		for j in range(rows):
			if a[j][i] == 0:
				table[j][i] = table[j-1][i] + 1
	
	#Printtable(table,rows,cols)
				
	area = 0			
	for i in range(rows):
		#find max area for each row
		area = max(area, Histogram.maxArea(table[i]))			
	return area

a = [[0,0,0,0,1,0], [0,0,1,0,0,1], [0,0,0,0,0,0], [1,0,0,0,0,0], [0,0,0,0,0,1], [0,0,1,0,0,0]]
rows = len(a)
cols = len(a[0])
print("Max area of the rectangle=%d" % (BuildHistogram(a,rows,cols)))
