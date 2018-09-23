'''
Given a sorted list, remove the duplicates in place, return modified list and #unique values. 

Example: 
A = [1,1,2] should return length = 2, and A is now [1,2].
'''

'''
Notes:
- two pointers
   -- start pointer at the start of list
   -- end pointer at the end of list
- if duplicate
    - shift all values LEFT by one place
    - move duplicate to index location of end pointer
    - shift end pointer LEFT by one place
'''

def shift_left(ginput,start,end):
    for index in range(start,end+1):
        ginput[index-1] = ginput[index]
    

def iterate_list(ginput):
    start = 1
    end = len(ginput) -1
    while start <= end:
        if ginput[start] == ginput[start-1]:  #duplicate!
            tmp = ginput[start]
            shift_left(ginput,start+1,end)
            ginput[end] = tmp
            end = end - 1
        start = start + 1
    print(ginput[:end+1])

a = [1,2,3,3,4,5,7,7]
iterate_list(a)
