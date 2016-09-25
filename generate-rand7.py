#Generate rand7() using rand5()

'''
OBSERVATION:
There is no deterministic way of doing this - no GURANTEE than rand7() will return back in X calls


SOLUTION:
1. We need 3 bits to get 7  (111)
2. rand5() generates values 0 ,1, 2, 3, 4
   - if we ignore 4 there are equal number of odd and even values
   - rand5()%2 will return 0 or 1
   - rand7() can be constructed bit by bit from rand5()

REFERENCE:
1. https://www.quora.com/How-do-you-design-a-rand7-function-using-a-rand5-function

'''

import random
def rand5():
	return random.randrange(5) #genrates random value from 0 ... 4


def rand2():
	x = rand5()
	while x == 4:
		x = rand2()
	return x%2

def rand7():
	result = 4*rand2() + 2*rand2() + rand2()
	#IMPORTANT: handle 7
	if result == 7:
		return rand7()
	else:
		return result

for i in range(0,5):
	print(rand7())
