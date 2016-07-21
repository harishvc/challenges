#Find minimum number of denominations that make a given value and what are the denominations? 


#Solution 1: Recursion
import sys
def MinCoins(target,denominations):
	if target == 0:
		#case 1: valid path
		return 0
	elif target < 0:
		#case 2: invalid path
		return sys.maxsize
	else:
		#depth = minimum #ways to reach target, depth of the recursion tree
		depth = sys.maxsize
		for d in denominations:
			#denominations = 1,2,3
			#depth = 1 + min(f(target-1),f(target-2), f(target-3))
			 depth = min(depth,MinCoins(target-d,denominations))
		#IMPORTANT: Add +1 	 
		return 1 + depth 


#Solution 2: DP
#Time complexity: O(dt) d= # denominations, t = target
#OBSERVATION: 
# result holds ALL possible values of target starting 1 .... target(inclusive)
# if target is large and #denominations are less, more space is taken
def MinCoinsDP(target,denominations):
	#start from index=1 for simplicity
	#result = [0,1,2 ..... target]
	result = [sys.maxsize] * (target + 1)
	#result index stores the index value of minium denomination
	resultIndex = [sys.maxsize] * (target + 1)
	#base case: if target =0, valid path!
	result[0] = 0
	for partialSum in range(1,target+1):
		#depth = minimum #ways to reach target, depth of the recursion tree
		depth = sys.maxsize
		for d in denominations:
			#check if result[partialSum-d] < depth 
			#since result index stores the index value of minium denomination 
			if partialSum >= d and result[partialSum-d] < depth:
				depth = result[partialSum-d]
				#result index stores the index value of minium denomination
				resultIndex[partialSum] = denominations.index(d)
		result[partialSum] = 1 + depth
	return result[-1],resultIndex


def FindDenominations(target,denominations,resultIndex):
	result = []
	while target != 0:
		#result index stores the index value of minium denomination
		#find minium denomination
		d = denominations[resultIndex[target]]
		result.append(d)
		#calculate new target based on minimum denomination
		target = target - d
	return result



denominations  = [2,3,1]
target = 5


result, resultIndex = MinCoinsDP(target,denominations)
mindenominations = FindDenominations(target,denominations,resultIndex)

print("Minimum # of coins to make %d=%d" % (target,result))
print("Coins to make %d=%s" % (target,mindenominations))