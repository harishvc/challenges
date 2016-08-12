#Given target and possible values find #permutations to achieve the target

#Question: Find all possible paths
#Solution: Similar to tree traversal 
#Keep reducing the target value until the value == 0 or negative!
def AllPermutations(target,values,path,level,result):
	if target == 0:
		#case 1: valid path, return 1
		t = path[:level]
		t.sort()
		if t not in result:
			result.append(t)
		#IMPORTANT: return 1, valid path
		return 1
	elif target < 0:
		#case 2: invalid path, return 0
		return 0
	else:
		#case 3: continue to go further
		count = 0
		for d in values:
			#IMPORTANT: insert current value to path at level
			path.insert(level,d)
			#IMPORTANT: level+1
			#Add up all path where target==0
			count += AllPermutations(target-d,values,path,level+1,result)
		return count


def findPermutations(target,values):
	table = [0]*(target+1)
	#IMPORTANT: table[0] = 0 , valid path!!!
	table[0] = 1
	for t in range(1,target+1):
		for s in values:
			if t >= s:
				table[t] += table[t-s]
	#print(table)
	return table[target]

target = 12
values = [1,2,3,6]
result = []

#Recursive solution
#count = AllPermutations(target,values,[],0,result)
#for r in result:
#	print(r)
#print(count)

#DP Solution
print("#Permutations to get target %d using values %s = %d" % (target,values, findPermutations(target,values)))

