#Find the **number** of distinct substrings of a given string 


'''
REFERENCE:
1. https://www.quora.com/Given-a-string-how-do-I-find-the-number-of-distinct-substrings-of-the-string

OBSERVATION:
Looking through the prefix of each suffix of a string, you have covered all substring of a string

'''

#Longest Common Prefix
def LCP(a,b):
	ai = len(a)
	ac = 0
	bc = 0
	maxLength = 0
	while(ac < ai):
		if(a[ac] == b[bc]):
			maxLength +=1
			ac +=1
			bc+=1
		else:
			return maxLength
	return maxLength



def SubStringCount(a):
	SuffixArray =  [a[i:] for i in range(len(a))]
	SuffixArray.sort()
	count = 0
	for i in range(len(SuffixArray)):
        #Characters not part of the LCP contribute to unique substrings
		count += len(SuffixArray[i]) - LCP(SuffixArray[i-1],SuffixArray[i])
	return count

a = "BANANA"
print(a, ">>>", SubStringCount(a))
