#14. Matching Parenthesis

#Observation:
# 1. keep count of ( , )  and check at the end how much they added up to?
# 2. keep count of unbalanced parenthesis , add as you see a new one, subtract as you see ), at the end is the result zero or non-zero 
#Algorithm:
# 1. Read one character from the string
# 2. Count unbalanced parenthesis ( or ) ... ignore anything else
# 3. if count is zero ... balanced, if count is negative ... unbalanced, return
#Complexity: 
# Time complexity: O(n) where n is the number of parenthesis in a string
# Space complexity:
#Test cases: [ '((()!@#%^&* )   )' , '((()()' , '))))((', ')(' , '))))((((' , '((()))']
#Proof:
#Code:

def CheckString(input):
    CTR = 0            #count unbalanced parenthesis
    for index in range(len(input)):
        if (input[index] == "("):
            CTR += 1
        elif (input[index] == ")"):
            CTR -= 1
            if (CTR < 0): 
                print input , " unbalanced"
                return
    if CTR == 0:
        print input , " balanced"
    else:
        print input , " unbalanced"
        


input = [ '((()!@#%^&* )   )' , '((()()' , '))))((', ')(' , '))))((((' , '((()))']
for s in range(len(input)):
    CheckString(input[s])