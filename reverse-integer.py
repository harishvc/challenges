'''
Question: Reverse integer

Example: 123 => 321
         -456 => -654
'''

#solution 1
def ReverseInt(input,result):
    if (input <= 9):
        return (10*result) + input
    q = int(input/10)
    r = input%10
    result = (10*result) + r
    return ReverseInt(q,result)

#Solution 2
def reverseNumber(a,prod=0):
	if a <= 9:
		return a + prod
	else:
		prod = (prod + a%10) *10
		return(reverseNumber(a//10,prod))


inputs = [-91,-123,567]
prefix =""
for input in inputs:
    if (abs(input) != input):
        prefix="-"
    else:
        prefix =""
    print(input, "====> %s%d" % (prefix,ReverseInt(abs(input),0)))


