#Find minimum number of denominations that make a given value and what are the denominations? 

'''
OBSERVATION
1. Keep reducing the target value until the value == 0 or negative!
2. if value == 0 then permutation is valid!
3. If we start bottom up, we can compute #permutations from earlier computed values
'''


import sys
def minCoinsDenominations(target,denominations):
	table = [sys.maxsize] * (target+1)   #range from 1 .... target
	dtable = [sys.maxsize] * (target+1)  #min denomination index 
	table[0] = 0 #important: valid permutation
	for i in range(1,len(table)):
		for d in denominations:
			if i>=d:
				count = 1+table[i-d]
				if count < table[i]:
					table[i] = count
					dtable[i] = denominations.index(d)
	#print(table)
	#print(dtable)

	#Traverse the dtable to find min values
	result = []
	while target > 0:
		result.append(denominations[dtable[target]])
		target = target - denominations[dtable[target]]

	return table[-1],result	

denominations  = [1,2,3]
target = 5
result = []
min_coins, result = minCoinsDenominations(target,denominations)
print("min coins to make %d = %d" % (target,min_coins))
print("denominations to make %d = %s" %(target,result))
