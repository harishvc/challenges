'''
Find #steps to convert string1 to string 2 using operations insert,remove,replace
Reference: http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
'''

#Recurisve
#LD(a,b,i+1,j,sizea,sibeb) -> delete/remove
#LD(a,b,i,j+1,sizea,sibeb) -> insert/add
#LD(a,b,i+1,j+1,sizea,sibeb) -> replace 
def LD(a,b,i,j,sizea,sibeb):
	if (i == sizea):
		return j
	elif (j == sibeb):
		return i
	elif(a[i] != b[j]):
		return (1 + min( LD(a,b,i+1,j,sizea,sibeb),LD(a,b,i,j+1,sizea,sibeb),LD(a,b,i+1,j+1,sizea,sibeb)))
	else:
		return (min( 1+LD(a,b,i+1,j,sizea,sibeb), 1+LD(a,b,i,j+1,sizea,sibeb),LD(a,b,i+1,j+1,sizea,sibeb)))

#Time & Space complexity: O(m*n)
def DPTableDistance(a,b,sizea,sizeb):
	row = len(b)
	col = len(a)
	#DP Table
	table = [[ 0 for y in range(col+1)] for x in range(row+1)]
	#Initialze row
	for x in range(0,len(table[0])):
		table[0][x] = x
	#Initialze column
	for x in range(0,len(table)):
		table[x][0] = x
	for i in range(1,row+1):
		for j in range(1,col+1):
			if b[i-1] == a[j-1]:
				table[i][j] = table[i-1][j-1]
			else:
				table[i][j] = 1 + min (table[i-1][j],table[i][j-1],table[i-1][j-1])
	#print(table)
	return table[row][col]


a ="cat"
b ="kate"
print("%s -> %s = %d" % (a,b,DPTableDistance(a,b,len(a),len(b))))
