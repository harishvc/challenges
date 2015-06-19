#Question: Compute all permutations (anagrams) of a string 
#Time complexity: O(2^n), n is # elements

input='abc'
print("input >>>",input)

#Solution 1:
#Time complexity O(n!), space complexity O(n)
from itertools import permutations
perms = [''.join(p) for p in permutations(input)]
print("Permutations (solution 1) >>>>", perms)

    
#Source: http://www.jeremy-boyd.com/2010/10/18/compute-all-permutations-of-a-string-in-python/    
#Solution 2: Using recursion
def permute2(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            for perm in permute2(s[:i] + s[i+1:]):  #send characters on the left and right of i
                res += [c + perm]
    return res
print("Permutations (solution 2) >>>>",permute2('abc'))


    
