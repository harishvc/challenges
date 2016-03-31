#Find the longest repeating substring (longest substring of a string that occurs at least twice)

'''
NOTES
Reference: https://en.wikipedia.org/wiki/LCP_array
1. Suffix array represents the lexicographic rank of each suffix of an array
2. Longest Common Prefix (LCP) contains the maximum length prefix match between 
   two consecutive suffixes, after they are sorted lexicographically 

References:
1. http://www.geeksforgeeks.org/suffix-tree-application-3-longest-repeated-substring/
2.https://www.quora.com/Write-a-program-to-return-the-longest-repeating-substring-in-a-string
'''
def findLCP(a):
	lca = []
	lca.append(-1)
	for i in range(1,len(a)):
		if(a[i-1] in a[i]):
			lca.append(min(len(a[i-1]),len(a[i]))) 
		else:
			lca.append(0)
	return lca

myinput = ["ABABAB", "BANANA", "GEEKSFORGEEKS", "ABABABA", "ATCGATCGA"]
#myinput = ["BANANA"] #Incorrect!
for text in myinput:
	suffix = [text[i:] for i in range(len(text))]
	Sortedsuffix = sorted([text[i:] for i in range(len(text))])
	LCP = findLCP(Sortedsuffix)
	maxValue = max(LCP)
	maxIndex = LCP.index(maxValue)
	index = len(suffix[LCP[maxIndex]])
	print(text, ">>>", text[index:index+maxValue])
	#reset
	del suffix[::]
	del Sortedsuffix[::]
	del LCP[::]
