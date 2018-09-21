'''
Given some number of floors and 2 eggs, what is the minimum number 
#of attempts it will take to find out from which floor egg will break in the worst case.

REFERENCES:
1. https://www.interviewcake.com/question/python/two-egg-problem
2. https://www.mathsisfun.com/algebra/quadratic-equation.html
3. https://github.com/harishvc/challenges/blob/master/images/egg-drop-recursion.jpg
4. https://www.interviewcake.com/concept/java/triangular-series
'''

'''
ANALYSIS:
Solution 1: Apply Binary search concept
   -- By reducing the problem size by half in each iteration.
   -- if we start at floors//2 . We have two choices, the egg will break or not
      -- if egg breaks go down
      -- if egg does not break go up
   -- if the egg breaks at floor 99 , attempts for worst case is 50 (1+49)
   -- can do better than that?

Solution 2: Skip floors by a constant value? If so what is an optimal value?
    -- Break into small groups of 5 
        -- if the egg breaks at floor 99, attempts for worst case is 23 (19+4)
    -- Break into smaller group of 10
        -- if the egg breaks at floor 99, attempts for worst case is 19 (10+9)

Solution 3: Skip floors such that attempts for worst case is CONSTANT?
	-- Let's say if max attempts is 10
     -- if the egg breaks at floor 10, attempts for worst case is 10 (1+9), floors we can skip = 10
     -- if the egg breaks at floor 19, attempts for worst case is 10 (2+8), floors we can skip = 9
     -- if the egg breaks at floor 27, attempts for worst case is 10 (3+7), floors we can skip = 8
     -- #floors we can skip is n + n-1 + n-2  = total_number_of_floors (100)
        10 + 9 + 8 + 7 + ...... + 1 = 100   
        n +  n-1 + n-2 ..... +1 = n(n+1)/2 //TRIANGULAR series (starts with 1 and increases by 1)
        n(n+1)/2 = 100 
		    n^2 + n  = 200       
		    n^2 + n - 200 = 0   //QUADRATIC equation to solve for n
		    n =  -b +- sqrt(b^2 - 4ac) /2a   here a = 1, b =1 , c= -200
    -- By finding number of floors to skip (n)  you are also finding the min attempts that handles worst case    
'''

import math
def minAttempts(floors):
	t1 = math.sqrt((1^2) + (4*1*200))
	t3 = (-1 + t1)/2
	t4 = (-1 - t1)/2
	return math.ceil(max(t3,t4))

floors = 100
eggs = 2
print("Minimum attempts in worst case with %d eggs from %d floors = %d" % (eggs,floors,minAttempts(floors)))
