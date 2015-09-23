'''
Question: Given two numbers as list add them and return result as list. Example: [3,4] + [5,9] = [9,13]
'''

input1 = [6,4]
input2 = [5,9]
input3 = [a + b for a, b in zip(input1, input2)]
print(input3)
