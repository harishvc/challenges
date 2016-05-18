'''
Given unsorted list of positive and negative values check if there are 
consecutive values that add to to a given target

OBSERVATION:
1. unsorted list
2. postive and negative values
3. consecutive values
4. return TRUE or FALSE

Reference:
http://www.csinterview.com/find-continuous-subsequence-with-given-sum/

NOTES:
1. Si,j = Sj- Si-1
   Sum of values from index i to index j (inclusive) = sum of values from (0 to j) - (0 to i-1)
2. if Si,j is target (K)
3. Sj can be found as we iterate the input
4. continuous subarrays exisits if Si-1 = Sj - K
5. If we store sum of values at each index we can find Si-1
'''

def existTarget(a,target):
	cursum = 0     #current sum
	curhash = {}   #current hash
	for current in range(0,len(a)):
		#case 0: value == target
		if a[current] == target:
			print("case 0")
			return true

		#IMPORTANT!!!	
		#increment current sum		
		cursum += a[current]
		#hash of current sum and current index       
		curhash[cursum] = current
		  
		#case 2: sum == target
		if cursum == target:
			print("case 1")
			print(a[0:current+1])
			return True
		#case 3: check sum exisits
		elif (cursum - target) in curhash.keys():
			t = curhash[cursum - target] +1
			print(a[t:current+1])
			return True
	return False

a = [7,-3,-8,12,3,6]
target = 10
print("input >>> %s target=%d" % (a,target))
print("found? %s" % (existTarget(a,target)))