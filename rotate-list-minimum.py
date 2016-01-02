'''
Find the minimum value in a rotated sorted list.

Notes :notes:
1. In a sorted list left most value is less than right more value  [1,2,3,4,5]
2. In a rotated sorted list the left most value is greater than the right most value [3,4,5,1,2]
3. If left (L) and right (R) pointers are such that R > L then the section from L to R is SORTED!  
'''

#Solution 1: Visit each value in the list. When the new value is less than the old value you found the minimum
#Time Complexity: O(n)

#Solution 2: Apply the property of rotated list and BST to search only half of the list at any given time
def FindMin(input,start,end):
    #1 value
    if(start == end):
        return input[start]
    # 2 values
    elif (end-start == 1):
        print("Min =", min(input[start],input[end]))
        #return min(input[start],input[end])
    # 3+ values
    else:
        middle = start + int((end-start)/2)
        #sorted
        if(input[start] < input[middle]):
            FindMin(input,middle,end)
        else:
            FindMin(input,start,middle)


input = [4,5,6,7,0,1,2]
print("input >>>>", input)
FindMin(input,0,len(input)-1)
