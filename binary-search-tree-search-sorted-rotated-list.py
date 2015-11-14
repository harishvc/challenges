'''
Question: Search a target number in a rotated sorted list
'''

'''
Time complexity: O(logn)

Reference:
http://stackoverflow.com/questions/4773807/searching-in-an-sorted-and-rotated-array

Notes:
1. The interesting property of a sorted + rotated array is that when 
   you divide it into two halves, atleast one of the two halves will 
   always be sorted.
2. Comparing values we can discard one half of the array
'''
def BST(t2,target,start,end):
    mid = start + int((end-start)/2)
    #print("start=%d end=%d mid=%d" %(start,end,mid))
    if (start > end):
        return False
    elif (t2[mid] == target):
        return True
    #sorted
    elif( t2[start] <= t2[mid]):
        if (target >= t2[start] and target <= t2[mid]):
            return BST(t2,target,start,mid-1)
        else:
            return BST(t2,target,mid+1,end)
    #unsorted
    elif (target >= target[mid] and target <= target[end]):
        return BST(t2,target,mid+1,end)
    else:
        return BST(t2,target,start,mid-1)
    
t1 = [1,2,3,4,5]  #sorted list
t2 = [3,4,5,1,2]  #rotated sorted list
print("input ==>", t2)    
target = [4,50]
for x in target:
    result = BST(t2,x,0,len(t2)-1)    
    print("target=",x, " Found=", result)    