#Can the input word be split using space-separated sequence of dictionary words?

#Time Complexity: O(n^3)
#Reference: https://github.com/harishvc/challenges/blob/master/images/word-break.jpg
def wordBreak(a,d):
	size = len(a)
	end_index = [-1] * size
	for i in  range(0,size):
		#Generate suffix ending with the string
		if a[i:] in d:  
			#suffix ending in end match!
			end_index[i] = size-1 #record end index
			#optimize!
			#no need to go any further!
			break
		else:
			#generate suffix ending in index i
			for x in range(0,i+1):
				if a[x:i+1] in d:
					end_index[x] = i
	#print(end_index)

	#Each index has the end index of the word in the dictionary
	#Find end index of the index following end index!
	i = 0
	while i < size and end_index[i] != -1 :
		i = end_index[i] + 1
	return True if i == size else False


a = "leetcode"
d2 = [["leet", "code"], ["le","code","leet","etco","ode"]]
for d in d2:
	print("string=%s dictionary=%s  break?%s" % (a,d,wordBreak(a,d)))
