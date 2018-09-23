#Given target and possible values find 
  #1. Total permutations to achieve the target
  #2. All possible permutations


'''
OBSERVATION:
1. if we subtract possible values from target unit target ==0 the path is valid (valid permutation)
                     6
                 1/ 2\ 3\ 6\
                 /    \  \  \
                5     4  3   0  <- valid path (if target =0)
2. If we start bottom up, we can compute #permutations from earlier computed values
'''

#Solution: Dynamic Programming (bottom up)
def totalPermutations(target,values):
	table = [0]*(target+1)
	#IMPORTANT: table[0] = 1 , valid path!!!
	table[0] = 1
	for t in range(1,target+1):
		for s in values:
			if t >= s:
				table[t] += table[t-s]
	#print(table)
	return table[target]

#Python generator
def allPath(target,path,values):
	if target == 0:
		yield path
	else:
		for i in values:
			if target >= i:
				yield from allPath(target-i,path+[i],values)



target = 6
values = [1,2,3,6]
result = []

print("#Permutations to get target %d using values %s = %d" % (target,values, totalPermutations(target,values)))

print("\nall permutations")
for i in allPath(target,[],values):
	print(i)
