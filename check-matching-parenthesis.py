#Question: Check if a string containing parenthesis'()' is balanced, every '(' has a matching ')' to the right of it and no ')' is unmatched.
#Answer:
#1. Observation:
# 1.1 Keep count of number of occurrences & order of '(' & ')' parenthesis 
#  1.2 Count unbalanced '(' parenthesis  - add when you see '(', subtract when you see ')', at the end is the result zero or non-zero?
#  1.3 At any given time count of '(' is less than ')' the string is unbalanced - handle ')('  
#2. Algorithm:
# 2.1 Read one character from the string
# 2.2 Count unbalanced left parenthesis '('
#  2.1 unbalanced & return if # left parenthesis is less than # of right parenthesis
#  2.2 balanced if count is zero ... balanced
#  2.3 unbalanced if count is negative 
#3. Complexity: 
# 3.1 Time complexity: O(n) where n is the number of parenthesis in a string
# 3.2 Space complexity:
#4. Test cases: [ '((()!@#%^&* )   )' , '((()()' , '))))((', ')(' , '))))((((' , '((()))']
#5. Proof:
# ((()!@#%^&* )   )  balanced
# ((()()  unbalanced
# ))))((  unbalanced
# )(  unbalanced
# ))))((((  unbalanced
# ((()))  balanced
#6. Code:

def CheckMatchinParenthesis(input):
    CTR = 0 #count unbalanced ( parenthesis
    for index, character in enumerate(input):
        #print index, character
        if (character == "("):
            CTR += 1
        elif (character == ")"):
            CTR -= 1
            if (CTR < 0): 
                return ("unbalanced") # total ( is always greater or equal to )
    if CTR == 0:
        return ("balanced")
    else:
        return ("unbalanced")
        
input = [ '((()!@#%^&* )   )' , '((()()' , '))))((', ')(' , '))))((((' , '((()))']
for s in input:
    print s, CheckMatchinParenthesis(s)