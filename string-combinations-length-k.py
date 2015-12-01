'''
Question: Given a set of characters and a positive integer k, print all possible strings of length k that can be formed from the given set.

Reference: 
http://www.geeksforgeeks.org/print-all-combinations-of-given-length/

Example: 
input = 'ab' , k = 2
output = [aa , ab, ba, bb]

#combinations = n^k
'''


input = 'ab'
k = 2


def FindCombinations(input,k,prefix):
    if (k == 0):
        print(prefix)
        prefix = ""
        return
    
    for i in input:
        new_prefix = prefix + i
        FindCombinations(input,k-1,new_prefix)

print("All combinations for input >>>", input  , " & k=",k)
FindCombinations(input,k,"")