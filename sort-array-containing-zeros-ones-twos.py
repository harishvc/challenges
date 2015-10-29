'''
Question: Sort an array containing zeros,ones and twos
'''


#Solution 1: Use hash to keep count of zeros, ones and twos , then print hash
def HashSort(input):
    count = {}
    for x in a:
        if x in count.keys():
            count[x] += 1
        else:
            count[x] = 1

    if 0 in count.keys():
        for x in range(0,count[0]):
            print (0,end=" ")
    if 1 in count.keys():
        for x in range(0,count[0]):
            print (1,end=" ")
    if 2 in count.keys():
        for x in range(0,count[0]):
            print (2,end=" ")
    print()


#Solution 2: Use Dutch flag Sort algorithm
#http://rosettacode.org/wiki/Dutch_national_flag_problem#Python:_Sorted
#Since the sorted list will contain zeros on the left, twos on the right and ones in the middle
#use 3 pointers to keep track of bottom top (low), middle top (middle), top bottom (high)
def DFS(input):
    low = 0
    middle = 0
    high = len(input) -1
    while (middle <= high):
        new = input[middle]
        if (new == 0):
            input[low],input[middle] = input[middle], input[low]
            low += 1
            middle += 1
        elif (new == 1):
            middle += 1
        else: #2
            input[middle],input[high] = input[high],input[middle]
            high -= 1
    return input

input = [0,1,2,1,0]
print("Input ===>", input)
print("Sorted input ===>", DFS(input))