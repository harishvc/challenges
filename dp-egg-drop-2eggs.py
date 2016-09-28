#Given some number of floors and 2 eggs, what is the minimum number 
#of attempts it will take to find out from which floor egg will break in the worst case.

'''
REFERENCE:
1. https://www.interviewcake.com/question/python/two-egg-problem
2. https://www.mathsisfun.com/algebra/quadratic-equation.html
3. https://github.com/harishvc/challenges/blob/master/images/egg-drop-recursion.jpg


Solution 1: Apply Binary search concept
   -- By reducing the problem size by half in each iteration.
   -- if we start at floors//2 . We have two choices, the egg will break or not
      -- if egg breaks go down
      -- if egg does not break go up
   -- if the egg breaks at floor 50 , max attemps for worst case is 49
   -- can do better than that!

Solution 2: Escape floors by a constant value? If so what is an optimal value?
    -- Let's say we break into small groups of 5 . Drop egg on floor 5
        -- if egg breaks, max attempts for worst case is 4
        -- if does not break, we do next 5 , next 5 ,,,,,, 20 times!
        -- max attemps for worst case is 20
    -- Can we change the smaller group from 5 to 10?
        -- if egg breaks at floor 10, max attempts for worst case is 9
        -- if egg break at floor 21 .... , max attemps will be 12 
           1(10),2(20),3(30,breaks!),4 (29),5(28),6(27),7(26),8(25),9(24),10(23),11(22),12(21)
        -- if egg break at floor 31 .... , max attemps will be 13
           1(10),2(20),3(30),4(40,breaks!),5(39),6(38),7(37),8(36),9(35),10(34),11(33),12(32),13(31)
        -- max attempts INCREASES as we move up

Solution 3: Can we escape few floors each time such that max attempts is CONSTANT?
	-- Let's say if max attemps is 10
	    -- start at floor 10
		-- next iteration we start at floor 19 (not 20)
		-- following iteration we can then start at floor 28 (not 30)
		-- #floors we can escape is n + n-1 + n-2  (== total floors)
		-- n +  n-1 + n-2 ..... n(n+1)/2 
		n^2 + n = 200       //if total floors == 100
		n^2 + n - 200 = 0   //QUADRATIC equation to solve for n
		n =  -b +- sqrt(b^2 - 4ac) /2a   here a = 1, b =1 , c= -200
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
