#Given a list, identify two sub-lists with equal sum (balanced partition) 

'''
OBSERVATION:
1. Find all the subsets recursively
2. On the way back (from the last node) check the sum
3. Similar to POST ORDER traversal!

During each recursive call
  - Increment depth
  - Increment start
  - Decrement target
  - Add new node to visited node (at current depth)

REFERENCE:
1. http://www.geeksforgeeks.org/backttracking-set-4-subset-sum/
'''

'''
target  = sum for balanced partition
start   = start index
end     = end index
depth   = depth of the recursion tree
results = all the nodes visited so far
'''
def findAllBalancedPartitions(a,target,start,end,depth,result):
	#Edge case: sum = 0
	if target == 0 and start > 0:
		yield result[0:depth]
		return
	for i in range(start,end):
		#IMPORTANT: list insert modifies the list and returns None
		result.insert(depth,a[i])
		yield from findAllBalancedPartitions(a,target-a[i],i+1,end,depth+1,result)
	

a = [4,1,-5,6,-11,3]
print("Input >>>", a)
print("Listing all balanced partitions ...")
for x in findAllBalancedPartitions(a,sum(a)//2,0,len(a),0,[]):
	#find rest of the values
	y = [i for  i in a if i not in x]
	print(x,y)
