#Print string permutations with unique values
#Total #possibilities = n!


'''
NOTES:
1. Permutation relates to the act of arranging all the members of a set into some sequence or order
2. Permutation result has same length are original string (no empty string and strings of different length)
3. Permutation can be considered as a COMPLETE GRAPH TRAVERSAL problem without visiting any node twice
'''

#Solution 1: Graph traversal 
'''
1. Traversing a COMPLETE GRAPH

LIMITATION: 
Only work with unique characters

REFERENCE:
1. http://exceptional-code.blogspot.com/2012/09/generating-all-permutations.html
'''
#Time complexity: O(n!)
def findPermutations1(a,size,path,level,visited):
	if level == size:
		#IMPORTANT: Limit to SIZE!!!
		print("".join(path[0:size]))
		return
	for i in range(0,size):
		#a[i] is UNIQUE
		if visited.setdefault(a[i],False) == False:
			path.insert(level,a[i])
			visited[a[i]] = True
			findPermutations1(a,size,path,level+1,visited)
			#IMPORTANT: Avoid loops!!!
			visited[a[i]] = False


#Solution 2: DP
'''
OBSERVATION:
a    = [a]
ab   = [ab, ba]
abc  = [a +p(bc)] + [b +p(ca)] + [c + p(ab)]

This logic works with unique and duplicate values
'''
#Time complexity: O(n!)
def PermutationsDP(a):
	if len(a) == 1:
		#IMPORTANT: Return as list, simplify operations
		return [a] 
	else:
		t = []
		for i in range(len(a)):
			t1 = a[0:i] + a[i+1:]
			#IMPORTANT: unpack result from list, concatenate and store result in list
			t2 = [a[i]+t2 for t2 in PermutationsDP(t1)]
			t += t2
		return t

a = "abc"  
print("Permutations of %s >>>" % (a))

#findPermutations1(a,len(a),[],0,{})

print(PermutationsDP(a))

