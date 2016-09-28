#Given some number of floors and some number of eggs, what is the minimum number 
#of attempts it will take to find out from which floor egg will break in the worst case.


'''
NOTES:
1. There are 2 choices at each step
    - egg breaks
    - egg does not break
2. If egg breaks, you have one less egg and you move DOWN (current_floor - 1)
3. If egg does not break, #eggs does not change and you move UP to a new floor (total #floors - current)
4. Find max attempts (worst case) for each #2 #3
5. Find min of all possible attempts

REFERENCE:
1. https://www.youtube.com/watch?v=3hcaVyX00_4
2. https://prismoskills.appspot.com/lessons/Dynamic_Programming/Chapter_11_-_Egg_dropping_puzzle.jsp
3. http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
4. https://github.com/harishvc/challenges/blob/master/images/egg-drop-recursion.jpg
'''

import sys
def eggDropRecursive(eggs,floors):
	#IMPORTANT: Exit condition
	if floors == 0 or eggs == 1:
		return floors
	result = sys.maxsize
	#IMPORTANT: start=1, end=floor+1
	for current_floor in range(1,floors+1):
		#egg breaks: 1 less egg and current_floor-1 floors to check
		left = eggDropRecursive(eggs-1,current_floor-1)
		#egg does not break: # eggs doesn't change, floors-current_floor to check
		right = eggDropRecursive(eggs,floors - current_floor)
		#find max to handle worst case
		worst_case_attempts = max(left,right) + 1
		#final result is minimum of all worst cases!
		result = min(result,worst_case_attempts)
	return result


#Time Complexity: O(ef^2) , e = #eggs  f= #floors
#Auxiliary Space: O(ef)
def eggDropDP(eggs,floors):
	table = [[sys.maxsize for i in range(0,floors+1)] for j in range(0,eggs+1)]
	for e in range(1,eggs+1):
		for f in range(1, floors+1):
			#case 1: when egg =1
			if e == 1:
				table[e][f] = f
			#case 2: floor <= egg
			elif f <= e:
				table[e][f] = f
			#case 3: calculate from prior values
			else:
				for i in range(1,f):
					left = table[e-1][i-1]
					right = table[e][f-i]
					worst_case_attempts = max(left,right) + 1
					table[e][f] = min(table[e][f],worst_case_attempts)
	#print(table)
	return table[eggs][floors]


floors = 10
eggs = 2
print("Minimum attempts in worst case with %d eggs from %d floors = %d" % (eggs,floors,eggDropDP(eggs,floors)))

	
