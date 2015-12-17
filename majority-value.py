'''
Given a list of size n, find the majority element.You may assume that the list is non-empty and the majority element always exist in the list.

The majority element is the element that appears more than n/2  times.
'''


#Solution 1: Sort the list and find the middle value

#Solution 2: Visit each value in the list and store count in a hash. Return element when count > total/2

#Solution 3: Linear Time Majority Vote Algorithm
def FindMajority(input):
    result = 0
    count = 0
    for i in range(len(input)):
        if (count == 0):
            result = input[i]
            count  = 1
        elif (result == input[i]):
            count += 1
        else:
            count -= 1
    return result

input = [1,2,3,1,3,3,3]
print("input >>>", input)
print("majority =", FindMajority(input))