#Find minimum number of coins that make a given value

#Solution 1
#BRUT FORCE Algorithm
#Time complexity: O(d^t) (UPPER LIMIT), d= # denominations, t = target
# d choices at each recursion, not symmetric since choices are different
# d^t/max(d) (LOWER BOUND)
def findMin(denominations,target):
	minCount = None
	for value in denominations:
		if target-value == 0: return 1
		if target-value > 0:
			tmp = findMin(denominations,target-value)
			if minCount is None or tmp < minCount:
				minCount = tmp
	return minCount+1 #IMPORTANT!!!


#Solution 2: Add Memoization (cache, for lookup)
#Time complexity: O(dt) Best case scenario, d= # denominations, t = target
#OBSERVATION: 'target' hold possible value
def findMinWithCache(denominations,target,cacheCount):
	minCount = None
	#Check cache!!!
	if target in cacheCount:
		return cacheCount[target]
	for value in denominations:
		if target-value == 0: return 1
		if target-value > 0:
			tmp = findMinWithCache(denominations,target-value,cacheCount)
			if minCount is None or tmp < minCount:
				minCount = tmp
	#Update cache
	cacheCount[target] = minCount+1
	return minCount+1 #IMPORTANT!!!

#https://github.com/mission-peace/interview/blob/master/python/dynamic/coinchangingmincoins.py
#https://www.youtube.com/watch?annotation_id=annotation_2195265949&feature=iv&src_vid=Y0ZqKpToTic&v=NJuKJ8sasGk
#Solution 3:
def print_coins(R, coins):
    start = len(R) - 1
    if R[start] == -1:
        print("No Solution Possible.")
        return
    print("Coins that generate minimum:")
    while start != 0:
        coin = coins[R[start]]
        print("%d " % (coin))
        start = start - coin

#Time complexity: O(dt) Best case scenario, d= # denominations, t = target
#OBSERVATION: T holds ALL possible value (what is T is large?, recursive is better)
def min_coins2(coins, total):
	cols = total + 1
	T =[0 if idx == 0 else float("inf") for idx in range(cols)]
	#print("T >>>", T)
	R = [-1 for _ in range(total + 1)]
	#print("R >>>", R)

	for j in range(len(coins)):
		#print("T intermediate >>>", T)
		for i in range(1, cols):
			coin = coins[j]
			if i >= coin:
				if T[i] > 1 + T[i - coin]:
					T[i] = 1 + T[i - coin]
					R[i] = j

	#print("T >>>", T)
	#print("R >>>", R)
	return T[cols - 1],R


denominations  = [9, 6, 5, 1]
target = 11

#Solution #2
#cacheCount = {}
#print("Minimum # of coins =",findMinWithCache(denominations,target,cacheCount))
#for key in cacheCount:
#	print(key,cacheCount[key])

#DP Iterative solution

result, R = min_coins2(denominations,target)
print("Minimum # of coins =",result)
print_coins(R, denominations)

