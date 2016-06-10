#Given n stairs to reach the top and you can take 1 or 2 steps at each stair . Find all possible combinations  
#n=4 result=5 variations=(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
#http://www.geeksforgeeks.org/count-ways-reach-nth-stair/

#Find all possible combinations
def stairCombinations(n,result,rsize):
	if n-1 >= 0:
			result.insert(rsize,1)
			yield from stairCombinations(n-1,result,rsize+1)
	if n-2 >= 0:
			result.insert(rsize,2)
			yield from stairCombinations(n-2,result,rsize+1)
	#IMPORTANT: n==0 at the top of the stairs		
	if n == 0:
		#recursion stack
		#print(result)
		yield result[0:rsize]

n = 4
result = []
for c in stairCombinations(n,[],0):
	if c not in result:
		result.append(c)
print("n=%d #combinations=%d" % (n,len(result)))
print("combinations=%s" % (result))
