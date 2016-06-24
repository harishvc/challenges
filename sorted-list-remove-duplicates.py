'''
Given a sorted list, remove the duplicates in place, return modified list and #unique values. 

Example: 
A = [1,1,2] should return length = 2, and A is now [1,2].
'''

'''
NOTES
1. Since the list is sorted, you need to store the last value
2. If can either  start from start or end
3. Keep track of #items, #unique items
4. Pop #items - #unique items times!
'''

#Solution 1: Inefficient with space
#Start from the end
def RemoveDuplicates(input):
    length = len(input)-1
    distinctCount = length+1 #default length
    seen = None #last value seen
    while(length >= 0):
        #First time!
        if (seen is None):
            seen = input[length]
        #Distinct
        elif(input[length] < seen):
            seen = input[length]
        #Duplicate
        else:
            input.pop(length) #Inefficient, since there can be duplicates in the middle
            distinctCount -= 1
        length -= 1
    return(input,distinctCount)

#Solution 2:
#Iterate list once, have all the duplicated values at the end (ending at certain index)
#pop #items - #unique items times!

input = [1,2,3,3,4,5,7]
print("input >>>", input)
result,count = RemoveDuplicates(input)
print("modified list without duplicates >>>", result)
print("#distinct values=",count)
