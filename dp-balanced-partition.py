#Given a list, identify two sub-lists with equal sum (balanced partition)


import sys
sys.path.append("./mylib")
import doless

'''
NOTES: Using DP to solve
1. Find the smallest and largest sum possible
2. Initialize a 2d matrix where rows are range of possible values and cols are given values
   - Set initial value to "F" (False)
3. Fill each cell in the 2d maxtrix -> Can I get the sum (col value) using values in row(s)
4. There are 3 possibilities
   - if value == sum, result is True
   - if sum in col before can be calculated, then the result is True
   - Check if sum-value has already been computed!
5. Traverse 2d matrix bottom up. If the value is "F" (False) you stop!

REFERENCE:
1. http://www.skorks.com/2011/02/algorithms-a-dropbox-challenge-and-dynamic-programming/
'''

#Step 1: find smallest sum and largest sum
def small_large(a):
	small = None
	rangemax = None
	for i in range(len(a)):
		#small
		if small is None:
			small = a[i]
		elif a[i] < small:
			small = a[i]
		#rangemax
		if a[i] > 0 and rangemax is not None:
			rangemax += a[i]
		elif a[i] > 0:
			rangemax = a[i]
	return small,rangemax

#Step 2: Fill DP Table
def PartitionDP(a,prange,table):
	for i in range(len(a)):  #rows
		for j in range(len(prange)): #cols
			#case 1: value == sum
			if prange[j] == a[i]:
				table[i][j] = 'T'
			#case 2: sum in col before is True, so new cell is also True	
			elif  i>=1 and table[i-1][j] == 'T':
				table[i][j] = 'T'
			#case 3: Check if the new sum was already calculated before	
			#IMPORTANT: Handle invalid index value!!!
			else:
				col = -1
				try:
					col = prange.index(prange[j]-a[i])
				except Exception as e:
					col = -1
				#IMPORTANT: Go back one row
				row = i-1
				#IMPORTANT: Check if index is valid
				if row >=0 and col >=0:
					table[i][j] = table[row][col]
	#DP Table
	#doless.PrintMatrix(table)

#Step 3: Navigate the DP table to find values
def findValues(a,prange,table,target):
	result = []
	row = len(a)-1
	col = prange.index(target)
	while table[row][col] == "T":
		if row-1 >=0 and table[row-1][col] == 'T':
			row -=1
		else:
			result.append(a[row])
			col = prange.index(prange[col]-a[row])
			row -= 1
		if row < 0:
			break	
	return result


a = [1,-3,2,4]
#Step 1: find smallest sum and largest sum
smallValue,maxRange = small_large(a)
#Important +1 to include largest sum
maxRange += 1
#All possible sum ranges
prange = [i for i in range(smallValue,maxRange)]
#DP Table cols=sum ranges, rows=#values
table = [[ 'F' for i in range(abs(smallValue)+abs(maxRange))] for j in range(len(a))]
#Step 2: Fill DP Table
PartitionDP(a,prange,table)
#Step 3: Navigate the DP table to find values
result = findValues(a,prange,table,sum(a)//2)
#Find remaining values
result2 = [i for i in a if i not in result]
print("input >>> ",a, " can be split into >> ", result,result2)
