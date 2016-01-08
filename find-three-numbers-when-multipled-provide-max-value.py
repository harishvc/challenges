'''
Question: Write a function which takes in a list of integers and returns the highest positive product
possible by multiplying 3 distinct numbers. No sorting.
'''

def MaxPair(input):
    size = len(input) -1
    max = None
    for i in range(0,len(input)-2):
        a = i
        b = i+1
        c = size
        while (b < c):
            new = input[a] * input[b] * input[c]
            if (max is None or max < new):
                max = new
            c -= 1
    return max


input = [100,20,5,2]
print(input)
print("max product of 3 values = ", MaxPair(input))