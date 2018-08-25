#Can the input word be split using space-separated sequence of dictionary words?


'''
Time Complexity: O(n^2)
Reference: https://github.com/harishvc/challenges/blob/master/images/word-break.jpg

s = "leetcode"
mydict = ["leet", "code"]

          3   -1   -1    -1   7   -1  -1    -1
lookup = [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]
          l    e    e    t    c    o    d    e

i = 0, x = 0 
     >> leetcode
     >>> l
i = 1 , x = 0,1
     >> eetcode
     >>> le
     >>> e     
i = 2, x = 0,1,2
     >> etcode
     >>> lee
     >>> ee
     >>> e
i = 3, x = 0,1,2,3
    >> tcode
    >>> leet
    >>> eet
    >>> et
    >>> t
i = 4
    >> code
i = 5, x=0,1,2,3,4,5
    >> ode
    >>> leetco
    >>> eetco
    >>> etco
    >>> tco
    >>> co
    >>> o
'''

'''
`lookup` contains the end index of a word or -1
'''
def wordBreak(s,mydict):
	lookup = [-1] * len(s)
	size = len(s)
	for i in range(0,size):
		#O(n)
		if s[i:] in mydict:
			lookup[i] = size-1
		else:
			#O(n^2)
			for x in range(0,i+1):
				if s[x:i+1] in mydict:
					lookup[x] = i
	#print(lookup)

	i = 0
	while i < size and lookup[i] != -1 :
		i = lookup[i] + 1
	return True if i == size else False


a = "leetcode"
d2 = [["leet", "code"], ["le","code","leet","etco","ode"]]
for d in d2:
	print("string=%s dictionary=%s  break?%s" % (a,d,wordBreak(a,d)))

