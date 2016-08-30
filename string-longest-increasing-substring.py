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

#Length of the Longest Common Prefix
def MaxLength(a,b):
	ai = len(a)
	bi = len(b)
	ac = 0
	bc = 0
	maxLength = 0
	#compare 1 character from a and b
	while(ac < ai and bc < bi and a[ac] == b[bc]):
			maxLength +=1
			ac +=1
			bc +=1
	return maxLength

def findLCP(a):
	#Longest Common Prefix (LCP) contains the maximum length prefix match between 
    #two consecutive suffixes, after they are sorted lexicographically 
	lcp = []
	for i in range(0,len(a)):
		#find LCP between current suffix and it left neighbor
		lcp.append(MaxLength(a[i-1],a[i]))
	return lcp

myinput = ["ABABABA", "BANANA","GEEKSFORGEEKS", "ATCGATCGA"]
for text in myinput:
	#Step 1: Generate suffix array
	suffix = [text[i:] for i in range(0,len(text))]
	#Step 2: Sort suffix array
	Sortedsuffix = sorted([text[i:] for i in range(0,len(text))])
	#Step 3: Generate LCP array based on sorted suffix array
	LCP = findLCP(Sortedsuffix)
	#Step 4: Find max value from LCP
	maxValue = max(LCP)
	#Step 5: Find index of max value
	maxIndex = LCP.index(maxValue)
	#Generate longest repeating substring
	print(text, ">>>", Sortedsuffix[maxIndex][:maxValue])
	#reset
	del suffix[:]
	del Sortedsuffix[:]
	del LCP[:]
