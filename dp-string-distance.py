'''
Find #steps to convert string1 to string 2 using operations insert,remove,replace
Reference: http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
'''

#Recurisve
#DistanceRecursive(a,b,i-1,j) -> delete/remove
#DistanceRecursive(a,b,i,j-1) -> insert/add
#DistanceRecursive(a,b,i-1,j-1) -> replace 
'''
NOTES
1. Process one character at a time for each of the strings starting either from left or right
2. There are two possibilities for every pair of character being traversed.
   2.1 Characters are same -> check the next character
   2.2 Characters are not same -> either insert, delete or replace
3. Time complexity: O(2^n) , n is the length of the smallest string
   Worst case if no characters match the time complexity becomes O(n^3)
'''
def DistanceRecursive(a,b,i,j):
	if (i == 0):
		return j
	elif (j == 0):
		return i
	elif(a[i-1] != b[j-1]):
		return (1 + min (    
			#delete i
			DistanceRecursive(a,b,i-1,j),   
			#insert before i
			DistanceRecursive(a,b,i,j-1),   
			#replace
			DistanceRecursive(a,b,i-1,j-1) )) 
	else:
		return DistanceRecursive(a,b,i-1,j-1)


#Time & space complexity: O(m*n)
def DPTableDistance(a,b):
	row = len(a) + 1
	col = len(b) + 1
	#DP Table
	table = [[ 0 for y in range(col)] for x in range(row)]
	#Compare a[i] with b[j] -> character by character
	for i in range(row):
		for j in range(col):
			#case 1: row index = 0
			if i == 0:
				table[i][j] = j 
			#case 2: col index = 0
			elif j == 0:
				table[i][j] = i
			#case 3: a[i] = b[j]
			elif a[i-1] == b[j-1]:
				table[i][j] = table[i-1][j-1]
			#case 4: a[i] != b[j]
			else:
				table[i][j] = 1 + min (table[i-1][j],table[i][j-1],table[i-1][j-1])
	print(table)
	return table[i][j]

a ="cat"
b ="kate"
#print("%s -> %s = %d" % (a,b,DistanceRecursive(a,b,len(a),len(b))))
print("%s -> %s = %d" % (a,b,DPTableDistance(a,b)))
