#Print the Power Set

#The power set is the set of all subsets of a given set
#Power set is a set of all combinations of lengths from size=0 to set size


#http://stackoverflow.com/questions/32406934/recursive-python-function-returning-powerset-of-items
#https://www.reddit.com/r/learnprogramming/comments/140rf0/python_explain_this_power_set_code_to_me/

#Solution 1: Recursive
def PowerSet1(z):
    if not z: return [[]]
    return PowerSet1(z[1:]) + [[z[0]] + x for x in PowerSet1(z[1:])]

#Solution 2: Using Binary Counter
'''
REFERENCE:
1. http://www.geeksforgeeks.org/power-set/

NOTES:
Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111
Value of Counter           Subset
   000                     -> Empty set
   001                     -> a
   011                     -> ab
   100                     -> c
   101                     -> ac
   110                     -> bc
   111                     -> abc
'''
def PowerSet2(z):
	#2^n possbile combinations
	count = 2**len(z)  
	for i in range(count):
		#Convert i to 3 digit binary with preceding 0
		bin1 = format(i,'03b')
		result =[]
		#map each 1 in binary to corresponding index in z
		for b in range(len(bin1)):
			if bin1[b] == "1":
				result += z[b]
		#IMPORTANT: Empty set is a power set!!!
		if len(result) == 0:
			print("[]")
		else:
			print("".join(result))

#Solution 3: Dynamic Programming
#Time complexity: O(2^n)
'''
Observation:
1. a = ()     result = ()
2. a = (1)    result = (), (1)
    - clone result of a=() + add 1
3. a = (1,2)  result = (2), (2,1), (), (1)
    - clone result of a=(1) + add result=a(1)
'''
def PowerSet3(z):
	result = [[]]
	for i in range(0,len(z)):
		t2 = [ [z[i]] + t1 for t1 in result]
		result += t2
		#print(result)
	return result

z = ['a','b','c']
print("power set of >>>", z)

result = PowerSet3(z)
print(">>>",result)
