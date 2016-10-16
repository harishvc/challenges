
#Find the longest substring with non-repeating characters

'''
Notes
1. Use a dictionary to store character as key and index as value
2. If new character already exisits?
    - Was it part of old substring?
    - Is it part of new substring? + new maxlength + new start
   else:
   	 pass

'''

#Time and space complexity: O(n)
def longestSubstring(a):
	visited = {}
	startIndex = 0
	maxsize = 0
	endIndex = 0
	for i in range(0,len(a)):
		if a[i] in visited.keys():
			if visited[a[i]] >= startIndex:
				endIndex = i -1 #move back!
				maxsize = max(maxsize,(endIndex-startIndex+1))
				startIndex = visited[a[i]] + 1 #next character
		visited[a[i]] = i
		endIndex = i
	maxsize = max(maxsize,endIndex-startIndex+1)
	return maxsize

aa = ["abc","abcdcabe","abccdefgh", "aaaa"]
for a in aa:
	print("input=%s  length of longest unique substring=%d" %(a,longestSubstring(a)))	


