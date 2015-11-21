'''
Problem:  Given a list of integers return a list of integers that only occurred once in the argument (or print them)

Design:
1. Scan the list once and store number of occurrences (hashmap or red black tree). Time complexity O(n), Space complexity O(n)
2. Sort the list and return only unique integers. Time complexity O(n log n), space complexity is O(1)
3. Invert the index value and element value using maximum number of elements in the array. 
   Index position of the maximum quotient provides the number of repeating element. Time complexity O(n) and space is O(1). 
   Limitations based on the # values in the list. works if value is < number of elements in the list. Time complexity O(n), space complexity is O(1)
'''

input = [1,2,2,5]

'''
Questions to ask: 
1. Is the list sorted? No
2. Memory constraints? Yes
'''
#Code: Solution 2 (using using design #2)
def PrintUnique1(input):
    input.sort()
    seen = None
    for i in range(len(input)):
        if (seen is None or seen != input[i]):
            print(input[i])
            seen = input[i]

print("Input >>>", input)
print("Unique values ....")
PrintUnique1(input)


#Code: Solution 2 (using using design #1 and red black tree)
'''
Why red and black trees are better than hashtables?
Source: http://www.quora.com/Why-would-anyone-like-to-use-a-red-black-tree-when-a-hash-table-can-do-the-job-perfectly 
1. Simple memory management - simplifies error handling in concurrent code, less I/O hits, 
2. Consistent performance because rehashing (expanding the hash table's array) happens on some insertions.
   This is important in real-time systems where you want to provide bounds on how long each operation takes
3. Keys are sorted
'''
#https://bitbucket.org/mozman/bintrees
from bintrees import RBTree
def PrintUnique2(k,v):
    if (v == 1): #unique
        print(k) #print unique
#Initialize
tree = RBTree()        
#Insert
for x in input:
    if (tree.get(x)): #duplicate
         tree.insert(x,tree.get(x)+1) #increment occurrence
    else: #new
        tree.insert(x,1)
#Iterate        
tree.foreach(PrintUnique2,0)  #0=inorder