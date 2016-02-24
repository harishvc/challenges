#Question:Find all possible combinations for a given string
#Note: Two combinations are same if they contain same characters but may be in different locations

input = "abc"
#Solution 1: Iterative
def comb(s,result):
    for i,v1 in enumerate(s):
        result.append(v1)
        inc = 1
        t1 = s[i+1:]
        for inc in range(0,len(t1)):
            for j in range(0,len(t1),inc+1):
                result.append(v1+t1[j:j+inc+1])
    return result
print("solution 1 >>> ", comb(input,[]))

#Solution #2: List generators    
#Source: http://thecodegalaxy.blogspot.com/2011/11/combinations-permutations-and-python.html
def combinations(string):
     yield ''
     for i, d in enumerate(string):
             for comb in combinations(string[i+1:]):
                    yield d + comb

print("solution 2 >>> %s" % (input), end="")
for comb in combinations(input):                
    print(comb, end =",")
print("")    

def combinations3(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        res.append(s[0]) 
        for c in combinations3(s[1:]): 
            res.append(c)
            res.append(s[0] + c)
        return res
print("solution 3 >>>>",combinations3(input))


