'''
Question: Search in sorted list X for index i such that X[i] = i

Reference: http://stackoverflow.com/questions/4172580/interview-question-search-in-sorted-array-x-for-index-i-such-that-xi-i

Questions:
1. Are values in the list unique
2. Can values be negative?
3. HOW MANY i's are there in the list?

Solution 1:
Iterate the entire length of the list.
Time complexity: O(n)


Solution 2:
Modified solution 1 where if input[i] > i then i = input[i]  (since list is sorted)
and continue to iterate. Less comparisons but still navigate entire list.
Time complexity: O(n)

'''

#Solution 3: Modify binary search
#Time complexity: O(log n)
#Limitation: When there is 1  i in the list!
def ModifiedBinarySearch(input):
    low = 0
    high = len(input) -1
    while (low <= high):
        mid = int ((low+high)/2)
        if (input[mid] - mid == 0 ):
            #print(mid)
            #low = mid + 1
            return mid
        elif(input[mid] - mid < 0):
            low = mid + 1
        else:
            high = mid - 1
    



input = [-3,-1,0,3,5]
print("input >>>", input)
print("x[i] = i when i=", ModifiedBinarySearch(input))