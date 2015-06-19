#Question:Find all possible combinations for a given string
#Note: Two combinations are same if they contain same characters but may be in different locations

input = "abc"

#Solution #1    
#Source: http://thecodegalaxy.blogspot.com/2011/11/combinations-permutations-and-python.html
def combinations(string):
     yield ''
     for i, d in enumerate(string):
             for comb in combinations(string[i+1:]):
                     yield d + comb


print("combinations of %s (solution 1) >>>" % (input), end =" ")
for comb in combinations(input):                
    print(comb, end =" ")
print("")    
    
#Solution #2    
from itertools import combinations    
def combinations2(input):
    l = len(input)
    output = []
    for count in range(l):
        for combination in combinations(range(l), count+1):
            toutput = []
            input_as_list = list(input)  #convert string to list of characters
            for value in combination:
                toutput += str(input_as_list[value]) #convert character to string
            output.append("".join(toutput))  #convert list of characters to list of strings
    return output       
print("combinations of %s (solution 2) >>>" % (input), combinations2(input))
