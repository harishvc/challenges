#Split the input string into a space-separated words in a dictionary and find all sequences

#Solution: Dynamic Programming
'''
1. Keep track of the longest match seen so far!
2. ALOGITHM
   - Check all permutations with dictionary. If found update index positions as 1 in a lookup table
   - If you have -1 in the lookup table, you can't split the word!
   - Keep track of the start and end index in a list
'''
def canSplit2(word,dictionary):
	size = len(word)
	table = [-1]*size #lookup table. Inititalize -1
	result = [-1]*size #lookup table. Inititalize -1
	#step 1: Find all 
	for i in range(0,size):
		for j in range(i,size):
			if word[i:j+1] in dictionary:
				#print(word[i:j+1])
				for t in range(i,j+1):
					table[t] = 1
				#store start and end index
				result[j] = i
	
	#print(table)
	#print(result)

	#step 2
	if -1 in table:
		#not possible
		return False
	else:
		for i in range(0,size):
			if result[i] >= 0:
				start = result[i]
				end = i+1
				print(word[start:end])
		return True

a = "iloveapple"
d = ["i", "lov", "love", "apple"]
print("input >>> %s " %(a))
print("All possible words ...")
canSplit2(a,d)