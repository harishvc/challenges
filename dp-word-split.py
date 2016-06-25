#Can the input word be split using space-separated sequence of dictionary words? 

#Solution 1: simple. Will **not** work if dictionary contains more than suffix of a word
def canSplit1(a,d,start,end):
	current = start
	while current < end:
		if a[start:end] in d:
			return True
		elif a[start:current+1] in d and a[current+1:end] in d:
			return True
		elif a[start:current+1] in d:
			current +=1
			start = current
		else:
			current +=1 
	return False

#Solution 2: Dynamic Programming
'''
1. Keep track of the longest match seen so far!
2. ALOGITHM
   - Check all permutations with dictionary. If found update index positions as 1 in a lookup table
   - If you have -1 in the lookup table, you can't split the word!
'''
def canSplit2(word,dictionary):
	size = len(word)
	table = [-1]*size #lookup table. Inititalize -1
	#step 1: Find all 
	for i in range(0,size):
		for j in range(i,size):
			if word[i:j+1] in dictionary:
				#print(word[i:j+1])
				for t in range(i,j+1):
					table[t] = 1
	#print(table)	
	#step 2
	if -1 in table:
		return False
	else:
		return True

a = "iloveapple"
d = ["i", "lov", "love", "apple"]
#print("input > %s canSplit? %s" % (a,canSplit1(a,d,0,len(a))))
print("input >>> %s canSplit? %s" % (a,canSplit2(a,d)))
