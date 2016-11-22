#Find all coin denominations that make a given value

'''
OBSERVATION
1. Keep reducing the target value until the value == 0 or negative!
2. if value == 0 then permutation is valid!
3. If we start bottom up, we can compute #permutations from earlier computed values
'''

#Solution: Dynamic Programming (bottom up)
def AllCoinPermutations(target,denominations,path):
	if target == 0:
		yield path
	else:
		for d in denominations:
			if target >= d:
				yield from AllCoinPermutations(target-d,denominations,path+[d])


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
for r in AllCoinPermutations(target,denominations,[]):
	print(r)	

#Print ONLY permutations with distinct combinations
#print("unique combinations ...")
#PrintUnique(result)
