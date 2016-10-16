#Longest Substring with At Most K Distinct Characters
#https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

'''
NOTES
1. Keep track of last index postion each character is appearing in a dictionary
2. If length of dictionary > K , we need to remove character(s)
	- since substrings are continuous, we remove the character furtherest way (low index)
	- update the start index of the new substring
'''
def longestSubstringK(a, K):
	max_size = 0     #max size!
	start_index = 0  #index position of the new substring 
	last_index = {}  #keep track of the last index of a character
	for i,c in enumerate(a):
		last_index[c] = i
		if len(last_index) > K:
			#remove the characters furthest away!
			lowest_index = min(last_index.values())
			del last_index[a[lowest_index]]
			start_index = lowest_index + 1
		max_size = max(max_size, i-start_index+1)
	return max_size


a = ["eceba", "ccebeb"]
K = 2
for a2 in a:
	print("%s  = %d" % (a2,longestSubstringK(a2,K)))
