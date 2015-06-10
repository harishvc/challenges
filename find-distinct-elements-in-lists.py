#Problem:  Given a list of integers return a list of integers that only ocurred once in the argument (or print them)

#Design:
#1. Scan the list once and store (hashmap) how often an iteger ocurrs and print the result. Time complexity O(n), Space complexity O(n)
#2. Sort this list and return only unique integers. Time complexity O(nlog n), space complexity is O(1)
#3. Inversion by changing the index value and element value using maximun number of elements in the array. Index position of the maximum quotient provides the number of repeating element. Time complexity O(n) and space is O(1). Limitations based on the value in the list. works if value is < number of elements in the list.

input = [1,2,2,5]

#Code: Solution 2
def PrintUnique(a):
    a.sort()  #sorting the array
    seen = a[0] #first value in list
    count = 0
    for i in range(len(a)):
        if (a[i] == seen): 
            count += 1    
        else: #new
            if (count == 1):
                #unique
                print(seen)
            seen = a[i]
            count = 1  #first time
        if (len(a)-1 == i and count == 1):   #last element in the list is unique
            print(seen)

PrintUnique(input)

# #TODO
# #4. Create a red and black tree using elements as key. Time complexity O(n), space complexity is O(n)
# from bintrees import RBTree
# tree = RBTree()
# for x in input:
# 	tree.insert(x,"1")  #default value is 1
# print(tree.iter_items)  #key and value pair is printed out.
