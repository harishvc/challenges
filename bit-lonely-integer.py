#Given a list of repeating integers find the lonely integer
#
#Example: [2,3,4,2,4] result=3

'''
NOTES: 
Limitations of using XOR 
1. Repeating values have to be even
2. There can only be one lonely integer  
'''
def LonelyInteger(b):
    t = list(b)
    result = None
    for x in t:
        if result is None:
            result = x
        else:
            result ^= x
    return result

values = [2,3,4,2,4]
print("input=%s lonely integer=%d" %(values,LonelyInteger(values)))