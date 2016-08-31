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
1. input = a       result = [[], [a]]
2. input = a,b     result = [[], [a], [b], [a,b]]
   >> p(a),p(a)+b
3. input = a,b,c   result = [[], [a], [b], [a,b], [c], [c,a], [c,b], [c,b,a]]
   >> p(a,b),p(a,b)+c
'''
def PowerSet3(z):
	#IMPORTANT: [[]]
	result = [[]]
	for i in a:
		tmp= [r+[i] for r in result]
		result += tmp
	return result

z = ['a','b','c']
print("power set of >>>", z)

result = PowerSet3(z)
print(">>>",result)
