#Print string combinations on length K

'''
NOTES:
Combination can be considered as a COMPLETE GRAPH TRAVERSAL problem without 
repeating characters in a different order - stop recursing branches with repeated characters.
'''

#Solution: Graph traversal 
'''
1. Traversing a COMPLETE GRAPH
2. LIMITATION:
   - Does not handle duplicates
   - Repeating values

REFERENCE:
1. http://exceptional-code.blogspot.com/2012/09/generating-all-permutations.html
'''

def findCombinations(a,k,start,count,path,result):
	if k == count:
		result.append(path[0:k])
		return
	for i in range(start,len(a)):
		#Avoid duplicate values
		if count >  0 and path[count-1] == a[i]:
			continue
		path.insert(count,a[i])
		findCombinations(a,k,start+1,count+1,path,result)

def mysort(self):
	self.sort()
	return self

a = "abc"  
k = 2
result = []
print("Combinations of %s of size=%s >>>" % (a,k))
findCombinations(a,k,0,0,[],result)

#Remove duplicates
#1: Sort
result.sort(key=mysort)
#2. convert to tuple and put them in a set
s = set(map(tuple,result))
print(s)