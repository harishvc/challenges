#Can the input word be split using space-separated sequence of dictionary words? 

'''
NOTES
Solve using Dynamic Programming
1. Use two loops - forward and backward
     - forward: check new word is dictionary
     - backward: check if new word can be split into **TWO** words based on 
       what we have seen and recorded so far 

REFERENCE
1. https://www.youtube.com/watch?v=WepWFGxiwRs
2. https://codesays.com/2014/solution-to-word-break-by-leetcode/

Time complexity: O(n^2)
Space complexity: O(n)
'''

def wordSplit(a,d):
	size = len(a)
	table = [False] * size
	for i in range(0,size):
		#case 1: Best case - word found!
		if a[:i+1] in d:
			table[i] = True
			continue
		#word not found: Can the new word be split into 
		#TWO words based on "what we have seen and recorded so far"?
		for j in range(i):
			#case 2: prefix not found!
			if table[j] == False:
				continue
			#case 3: prefix found, is suffix in dictionary?
			elif a[j+1:i+1] not in d:
				continue
			#case 4: word can be split into prefix and suffix found in dictionary
			else:
				table[i] = True
				break
	print(table)
	#return last index value
	return table[-1]


a = "iloveapple"
d = ["i", "lov", "love", "loveapple"]
print("input >>> %s canSplit? %s" % (a,wordSplit(a,d)))