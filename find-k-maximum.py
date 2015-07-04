'''
Question: Find kth largest element in an unsorted list.
'''

def BuildHeapMinTMP(A,k):
    TMP = []
    #Since k is small than len(A), append the first k elements to temporary list
    for i in range(0,k):
        TMP.append(A[i])
    #Create min heap for the first k elements
    BuildHeapMin(TMP,k-1)
    #TMP[0] has the smallest element
    #Iterate through rest of the elements (k+1 ... n) in 'A'
    #if 'A' has element greater than TMP[0] copy to TMP[0] and precolate down 
    for j in range(k,len(A)):
        if (A[j] > TMP[0]):
            TMP[0] = A[j]
            percolateDownMin(TMP, 0, k-1)
    return TMP


def BuildHeapMin(TMP,length):
  #length = len(TMP) -1
  lastParent = length // 2
  for i in range (lastParent, -1, -1):
      percolateDownMin(TMP, i, length)    
    
#MIN heap: Modified percolateDown to skip branch already heapified
def percolateDownMin(TMP, ParentIndex, Size):
  MaxChildIndex = 2 * ParentIndex + 1  #child on left
  while MaxChildIndex <= Size:
    # right child exists and is value of right child larger than left child
    if (MaxChildIndex < Size) and (TMP[MaxChildIndex] > TMP[MaxChildIndex + 1]):
        MaxChildIndex += 1
    # child node has value larger than parent
    if TMP[MaxChildIndex] < TMP[ParentIndex]:
        swap(TMP, MaxChildIndex, ParentIndex)
        # move down to largest child
        ParentIndex = MaxChildIndex
        MaxChildIndex = 2 * ParentIndex + 1
    else:
        #parent node has value greater than child node
        #no need to percolate down - heapify on linear time!
        return  # force exit


def swap(TMP, x, y):
  temp = TMP[x]
  TMP[x] = TMP[y]
  TMP[y] = temp  


#Reference:http://www.crazyforcode.com/TMPth-largest-smallest-element-array/
'''
#Solution 1:
1. Turn input into heap and heap sort. Time complexity = O(nlogn)
2. Find kth largest = O(1) ~ constant time
3. Time complexity = O(nlogn)

#Solution 2:
1. Build MAX heap . Time complexity = O(n)
2. Perform delete operations on the MAX heap. Time complexity = O(k log n)
3. Time complexity = O(n + klogn)

#Solution 3: 
1. Store first k elements in a temporary list
2. Build a MIN heap for the first k elements. Time complexity = O(k)
3. Build a heap for the remaining n-k elements O(n-k log k) only if element in n is > k[0] (MIN heap)
4. Time complexity = O(k + n-klogk) ~ linear time if k is too small
5. Space complexity = O(k)

#Solution 4:
If k is approximately equal to n, the input can be sorted  using linear sorting algorithms
to find the kth largest. Time complexity = O(n)
'''
#Solution: 3    
B = [34,1,99,99,35,1]
print("input >>>>", B)
for i in range(1,len(B)+1):
    TMP = []
    TMP = BuildHeapMinTMP(B,i)
    print(i ," largest is ", TMP[0] , " minheap >>>", TMP) 