'''
Question: Given a string where each character can be [0-9] or [+-*] find the result (hint: stack calculator)
'''

#http://stackoverflow.com/questions/22579121/stack-calculator-postfix-python
def calculate(inputs):
    stack = []
    for a in inputs:
        if type(a) is int:
            stack.append(a)
            continue

        op1, op2 = stack.pop(), stack.pop()

        if a == '+':
            stack.append(op2 + op1)
        elif a == '-':
            stack.append(op2 - op1)
        elif a == '*':
            stack.append(op2 * op1)
        elif a == '/':
            stack.append(op2 / op1)

    return stack.pop()

input = [[1, 2, '*', 3, '-'], [1, 2, '+', 3, '*'],[1, 2, '*', 3, '-', 2, '*', 5, '+']]
for x in input:
    print(x , " = ", calculate(x))
          
    