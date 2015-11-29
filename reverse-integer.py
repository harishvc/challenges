'''
Question: Reverse integer

Example: 123 => 321
         -456 => -654
'''

def ReverseInt(input,result):
    if (input <= 9):
        return (10*result) + input
    q = int(input/10)
    r = input%10
    result = (10*result) + r
    return ReverseInt(q,result)

inputs = [-91,-123,567]
prefix =""
for input in inputs:
    if (abs(input) != input):
        prefix="-"
    else:
        prefix =""
    print(input, "====> %s%d" % (prefix,ReverseInt(abs(input),0)))


