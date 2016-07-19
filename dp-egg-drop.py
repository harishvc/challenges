#Given some number of floors and some number of eggs, what is the minimum number 
#of attempts it will take to find out from which floor egg will break.


'''
NOTES:
1. if egg break at 
    - floor 0 we found the floor
    - floor > 0 , we need to find the "critical floor" BELOW with ONE LESS egg
2. if egg does not break
    - we need to find the "critical floor" ABOVE with N eggs
3. if #eggs = 0:
	- return #floors traversed
4. if #floor < #eggs:
	- return #floors

REFERENCE:
1. https://www.youtube.com/watch?v=3hcaVyX00_4

'''

#Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. 
#The problem is not actually to find the critical floor, but merely to decide floors from which eggs should be dropped so that total number of trials are minimized
#


import sys

#Recursive solution
def eggDropRecursive(n,k):
  if k <=1:
  	return k
  if n == 1:
  	return k
  count = sys.maxsize
  for i in range(1,k):
  	left = 0
  	right = 0
  	iMax = 0
  	#print("i=%d left=%d right=%d  iMax=%d count=%d" % (i,left,right,iMax,min(count,iMax)))
  	left  = eggDropRecursive(n-1,i-1)
  	right = eggDropRecursive(n,k-i)
  	iMax = max(left,right)
  	#print("\ti=%d left=%d right=%d  iMax=%d count=%d" % (i,left,right,iMax,min(count,iMax)+1))
  	count = min(count,iMax)
  return count+1

#Dynamic Porogramming
def eggDropDP(eggsCount,floorsCount):
	#DP Table
	#rows = #eggs
	#cols = #floors
	#Add +1 to rows and cols to simplify code
	minAttempts = [[sys.maxsize for i in range(floorsCount+1)] for j in range(eggsCount+1)]

	for i in range(1,eggsCount+1):
		for j in range(1,floorsCount+1):
			#case 1: #eggs = 1, #attempts=#eggs
			if i == 1:
				minAttempts[i][j] = j
			#case 2: #stairs <= #eggs	
			elif j<= i:
				minAttempts[i][j] = j
			#case 3:
			else:
				#tmp = table[i-1][j-1]
				for x in range(1,j):
					tmp = 1 + max(minAttempts[eggsCount-1][x-1],minAttempts[eggsCount][j-x])
					minAttempts[i][j] = min(minAttempts[i][j],tmp)

	#print(minAttempts)				
					
	return minAttempts[i][j]
					

n =2  #eggs count
k =6  #floors count

#print(eggDropRecursive(n,k))

print(eggDropDP(n,k))
