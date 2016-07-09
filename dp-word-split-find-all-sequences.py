#Can the input word be split using space-separated sequence of dictionary words? 

'''
NOTES:

Solve using Dynamic Programming
1. Use two loops - forward and backward
     - forward: check new word is dictionary
     - backward: check if new word can be split into **TWO** words based on 
       what we have seen and recorded so far 
     - keep track of the start index positions of match

REFERENCE
1. https://www.youtube.com/watch?v=WepWFGxiwRs
2. https://codesays.com/2014/solution-to-word-break-by-leetcode/

Time complexity: O(n^2)
Space complexity: O(n)
'''

def wordSplit(a,d):
	size = len(a)
	table = [-1] * size
	for i in range(0,size):
		#case 1: Best case - word found!
		if a[:i+1] in d:
			table[i] = 0 #start index of match!!
			continue
		#word not found: Can the new word be split into 
		#TWO words based on "what we have seen and recorded so far"?
		for j in range(0,i):
			#case 2: prefix not found!
			if table[j] == -1:
				continue
			#case 3: prefix found, is suffix in dictionary?
			elif a[j+1:i+1] not in d:
				continue
			#case 4: word can be split into prefix and suffix found in dictionary
			else:
				assert table[j] != -1, "Error 1"
				assert a[j+1:i+1] in d, "Error 2"
				#start index of match!!
				#IMPORTANT: j+1 
				table[i] = j+1 
				break
	#print(table)
	#each positive index position in table will have the start position of word in dictionary! 
	return table

def printWords(a,table):
	for i in range(0,len(table)):
		if table[i] > -1:
			start = table[i]
			#Important: i+1
			end = i + 1
			print(a[start:end])

a = "iloveapple"
d = ["i", "lov", "love","apple"]
print("input >>> %s" % (a))
print("words ...")
printWords(a,wordSplit(a,d))