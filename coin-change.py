#Find all coin denominations that make a given value

#Solution: Similar to tree traversal 
#Keep reducing the target value until the value == 0 or negative!
def AllCoinPermutations(target,denominations,path,level,result):
	if target == 0:
		#case 1: valid path
		result.append(path[:level])
		return 0
	elif target < 0:
		#case 2: invalid path
		return 
	else:
		#case 3: continue to go further
		for d in denominations:
			#IMPORTANT: insert current value to path at level
			path.insert(level,d)
			#IMPORTANT: level+1
			AllCoinPermutations(target-d,denominations,path,level+1,result)
		return  

#Print ONLY permutations with distinct combinations
def PrintUnique(result):
	def mysort(self):
		self.sort()
		return self
	#1: sort	
	result.sort(key=mysort)
	result2= []
	for x in result:
		#2. store unique ones in result2
		if x not in result2:
			result2.append(x)
	for s in result2:
		print(s)


#OBSERVATION: Order of denominations does not matter
denominations  = [2,3,1]
target = 5
result = []
print("All coin denominations that add up to %d" % (target))
AllCoinPermutations(target,denominations,[],0,result)

#Print ONLY permutations with distinct combinations
#PrintUnique(result)

for r in result:
	print(r)