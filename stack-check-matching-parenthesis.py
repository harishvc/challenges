'''
Question: Check if a string containing parenthesis'()' is balanced, every '(' has a matching ')' to the right of it and no ')' is unmatched.

Test cases: [ '((()!@#%^&* )   )' , '((()()' , '))))((', ')(' , '))))((((' , '((()))']

Proof:
 ((()!@#%^&* )   )  balanced
 ((()()  unbalanced
 ))))((  unbalanced
 )(  unbalanced
 ))))((((  unbalanced
 ((()))  balanced
'''


'''
Solution 1: Iterate and keep count

Algorithm:
1. Read one character from the string
2 Count unbalanced left parenthesis '('
3. unbalanced if # left parenthesis is less than # of right parenthesis
4. balanced if count is zero ... balanced
5. unbalanced if count is negative 

Time complexity: O(n)
Space complexity: O(1)
'''
def CheckMatchinParenthesis1(input):
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
        
    
'''
Solution 2: Iterate, store left parenthesis in stack, pop stack on right parenthesis

Algorithm:
1. Push left parenthesis '(' in stack
2. Pop when right parenthesis '(' is found
3. Pop error - unbalanced
4. Size of stack after iteration is > 0 then unbalanced

Time complexity: O(n)
Space complexity: O(n)
'''
def CheckMatchinParenthesis2(input):
    import sys
    sys.path.append("./mylib")
    import Stack
    demoStack = Stack.Stack()
    for entry in input:
        if (entry == '('):
            demoStack.push(entry)
        elif (entry == ')'):
            if (demoStack.pop() == -1):
                return ("unbalanced")
                exit
    #Check is stack is empty - more left parenthesis
    if (demoStack.mysize() == 0):
        return ("balanced")
    else:
        return ("unbalanced")


input = [ '((()!@#%^&* )   )' , '((()()' , '))))((', ')(' , '))))((((' , '((()))']
for s in input:
    print(s, CheckMatchinParenthesis1(s))
    print(s, CheckMatchinParenthesis2(s))
    print("~~~~")  
    
     