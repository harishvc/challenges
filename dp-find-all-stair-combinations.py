#Given n stairs to reach the top and you can take 1 or 2 steps at each stair . Find all possible combinations  
#n=4 result=5 variations=(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
#http://www.geeksforgeeks.org/count-ways-reach-nth-stair/

#Find all possible combinations

def stairCombinations(n,path,steps=None):
	if n ==0:
		yield path+[steps]
	elif n > 0:
		if steps is not None:
			yield from stairCombinations(n-1,path+[steps],1)
			yield from stairCombinations(n-2,path+[steps],2) 
		else:
			yield from stairCombinations(n-1,path,1)
			yield from stairCombinations(n-2,path,2) 

n = 4
print("Total #stairs=", n)
print("All possible combinations ...")
for i in stairCombinations(n,[]):
	print(i)
