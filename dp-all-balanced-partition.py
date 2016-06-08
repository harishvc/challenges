#Given a list, identify two sub-lists with equal sum (balanced partition) 



'''
OBSERVATION:
1. Find all the subsets recursively
2. On the way back (from the last node) check the sum
3. Similar to POST ORDER traversal!

REFERENCE:
1. http://www.geeksforgeeks.org/backttracking-set-4-subset-sum/
'''

'''
a = input list
result = store nodes along the recursion path
asize = size of input list
rsize = size of the result list
tsum = sum so far
nodes = #nodes seen so far
target = target
'''
def generateSubsets(a,result,asize,rsize,tsum,nodes,target):
	if tsum == target:
		#print (result[0:rsize])
		yield (result[0:rsize])
		#return
	else:
		for i in range(nodes,asize):
			#IMPORTANT: insert rather than append
			result.insert(rsize,a[i])
			yield from generateSubsets(a,result,asize,rsize+1,tsum+a[i],i+1,target)  

myinput = [4,1,-5,6,-11,3]
print("input >>> %s, Listing all sub-sets with sum=%d" % (myinput,sum(myinput)//2))
z = generateSubsets(myinput,[],len(myinput),0,0,0,sum(myinput)//2)
for i in z:
	print(i)


