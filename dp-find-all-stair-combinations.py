#Given n stairs to reach the top and you can take 1 or 2 steps at each stair . Find all possible combinations  
#n=4 result=5 variations=(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
#http://www.geeksforgeeks.org/count-ways-reach-nth-stair/

#Find all possible combinations
def stairCombinations(total_steps,path):
	if total_steps == 0:
		yield path
	elif total_steps == 1:
		yield path + [1]
	else:
		yield from stairCombinations(total_steps-1,path+[1])  #1 step
		yield from stairCombinations(total_steps-2,path+[2])  #2 step

n=4
print("stairs=%d" %(n))
print("all possible combinations")
for i in stairCombinations(n,[]):
	print(i)
