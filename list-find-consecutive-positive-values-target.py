'''
Given unsorted list of positive values check if there are 
consecutive values that add to to a given target

OBSERVATION:
1. unsorted list
2. postive values
3. consecutive values
4. return TRUE or FALSE
'''

'''
Algorithm:
1. start and current pointer set to index position 0
2. Iterate the list and advance current pointer
3. if sum > target
   - advance start until sum <= target and start <= current
'''
def existTarget(a,target):
	start = 0
	sum = 0
	for current in range(0,len(a)):
		#case 0:
		if a[current] == target:
			return True
		sum += a[current]
		#case 1: sum == target
		if sum == target:
			return True
		#case 2: sum > target	 
		elif sum > target:
			while sum >= target and start <= current:
				sum -= a[start]
				start += 1
				if sum == target:
					return True
		#case 3: sum < target
		else:	
			assert sum < target, "error"
	return False

a = [7,3,8,12,3,6]
target = 20
print("input >>> %s target=%d" % (a,target))
print("found? %s" % (existTarget(a,target)))
