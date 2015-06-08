#Question:Find all possible combinations for a given string

input = "abc"

#Source: http://thecodegalaxy.blogspot.com/2011/11/combinations-permutations-and-python.html
def combinations(string):
     yield ''
     for i, d in enumerate(string):
             for comb in combinations(string[i+1:]):
                     yield d + comb


print("combinations of %s >>>" % (input), end =" ")
for comb in combinations(input):                
    print(comb, end =" ")
print("")    
    
    