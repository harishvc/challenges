#Given a list, identify two sub-lists with equal sum (balanced partition)  

#Solution driven by dynamic programming
#http://www.skorks.com/2011/02/algorithms-a-dropbox-challenge-and-dynamic-programming/
def printTable(table):
	rows = len(table)
	cols = len(table[0])
	for i in range(rows):
		for j in range(cols):
			print(table[i][j], end="  ")
		print("")

#Return index position of a value or -1
def checkIndex(a,i):
	r = 0
	try:
		r = a.index(i)
	except:
		r =  -1
	return r

#Given a list find the smallest and largest range of values
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


def CalculateDPTable(a):
	#Step 1: Find the range - smallest and largest possible values
	smallest_sum,largest_sum = small_large(a)
	#Store the range in a list
	sum_range = [i for i in range(smallest_sum,largest_sum+1)]
	cols = len(sum_range)+1
	rows = len(a) +1
	#Initialize DP table
	#rows = given values
	#columns = range of values
	table = [['F' for i in range(cols)] for j in range(rows)]
    #Fill DP table
	for i in range(1,rows):
		for j in range(1,cols):
			#condition 1: row value = sum
			if (a[i-1] == sum_range[j-1]):
				table[i][j] = 'T'
			#condition 2: sum possible with earlier values of the sub-set
			elif table[i-1][j] == "T":
				table[i][j] = "T"
			#condition 3: if sum - new value is already a subset, then new sum is a subset
			else:
				t = sum_range[j-1]-a[i-1]
				r = checkIndex(sum_range,t)
				if r >= 0 and table[i-1][r+1] == "T":
					table[i][j] = "T"
	#printTable(table)
	return table,sum_range

#
def findBalancedSet(table,sum_range,a):
	i = len(table)-1
	j = sum_range.index(0) +1  #balanced sub-set
	result = []
	while i > 0 or j > 0:
		if table[i][j] == "T":
			if i-1 >= 0 and table[i-1][j] =="T":
				i -= 1
			else:
				result.append(a[i-1])
				j = sum_range.index(sum_range[j-1]-a[i-1]) + 1
		else:
			break
	return(result[::-1])





a = [1,-3,2,4]
table,sum_range = CalculateDPTable(a)
print("input=%s  balanced sub list=%s" % (a,findBalancedSet(table,sum_range,a)))
