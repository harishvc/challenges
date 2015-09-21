'''
Question: Check if a string contains matching parenthesis, square brackets and curly brackets is balanced
'''


'''
Solution 1: Iterate and keep count
Time complexity: O(n)
Space complexity: O(1)
'''

    
'''
Solution: Iterate, store left tags in stack, pop stack on right tags

Algorithm:
1. Push left parenthesis '(' in stack
2. Pop when right parenthesis '(' is found
3. Pop error - unbalanced
4. Size of stack after iteration is > 0 then unbalanced

Time complexity: O(n)
Space complexity: O(n)
'''
def CheckMatchingTags(input):
    import sys
    sys.path.append("./mylib")
    import Stack
    demoStack = Stack.Stack()
    match = {'}':'{', ')':'(', ']':'['}
    for entry in input:
        if (entry == '('):
            demoStack.push(entry)
        elif (entry == '{'):
            demoStack.push(entry)
        elif (entry == '['):
            demoStack.push(entry)
        elif (demoStack.peek() == match[entry]):
            if (demoStack.pop() == -1):
                return ("unbalanced")
                exit
    #Check is stack is empty - more left parenthesis
    if (demoStack.mysize() == 0):
        return ("balanced")
    else:
        return ("unbalanced")


input = [ '([]){}', '([])}{', '([]{}']
for s in input:
    print(s, CheckMatchingTags(s))
    print("~~~~")  
    
     