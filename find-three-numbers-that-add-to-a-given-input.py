'''
Question: Given a list and sum. Find 3 numbers in the list that add up to the given sum.
'''

'''
Solution1: Brut-force
1. Run 3 loops to find sum
2. Time complexity: O(n^3)


Solution 2:
Reference: http://stackoverflow.com/questions/2070359/finding-three-elements-in-an-array-whose-sum-is-closest-to-an-given-number#

Step 1: sort the list . nlog(n)
Step 2: initialize three pointers i,j,k and move them
 i = start of list
 j = next position after i
 k = end of list
Step 3: Iterate throught the list such that a[i]+a[j]+a[k] = 3sum or while k>= j
 if 3sum is > sum, increment k
 if 3sum is < sum, increment j
 
Time complexity: nlogn + O(n^2)
'''
#Finds the first match and does not handle duplicates - inaccurate!
def findNumbers(input,sum):
    input.sort()
    size = len(input)
    #print (input)
    for i in range (0,size):
        j = i+ 1
        k = size-1
        while (k>j):
            Tsum = input[i] + input[j] + input[k]
            if (Tsum == sum):
                print (input[i],input[j],input[k])
                return
            elif (Tsum > sum):
                k -= 1
            else:
                j += 1
    print("None")


'''
Questions to ask:
a. Is the input sorted? No
b. Are there duplicates? Yes
c. Can the triplets get printed as they are found? No  Return list with triplets

Solution 3: Modified solution #2 to handle duplicate values.
Time complexity: nlogn + O(n^2) , n is #unique values

Reference:
http://www.programcreek.com/2012/12/leetcode-3sum/
'''
#Handle duplicate values
def findNextb(b,c,input):
    while(b < c and input[b] == input[b-1]):
        b +=1
    return b

#Handle duplicate values
def findNextc(b,c,input):
    while(b < c and input[c] == input[c+1]):
        c -=1
    return c
   
def find3Numbers(input,sum):
    result = []
    length = len(input)
    #Validation
    if (length <= 2):
        return result
    #Step 1: Sort the input
    input.sort()
    #print("sorted .....", input)
    #Step 2: Iterate the input with 2 pointers
    for i in range(length-2):
        #Handle duplicates
        if (i == 0 or (input[i] > input[i-1])):
            a = i
            b =  i + 1
            c = length -1
            #a + b + c = sum
            #b + c  = sum - a
            wanted = sum - input[a]      
            #print("a=%d b=%d c=%d wanted=%d" %(a,b,c,wanted))
            while(b < c):
                #print("checking .....",input[b], input[c])
                bc = input[b] + input[c]
                #Match
                if (bc == wanted):
                    result.append([input[a],input[b],input[c]])
                    b += 1
                    c -= 1
                    #Duplicate values
                    b = findNextb(b,c,input)
                    c = findNextc(b,c,input)
                #sum of b+c is less, find next greater value
                elif( bc < wanted):
                    b += 1
                    #Duplicate values
                    b = findNextb(b,c,input)
                #sum of b+c is more, find next lesser value    
                else:
                    c -=1
                    #Duplicate values
                    c = findNextc(b,c,input)
    return result
   
input = [-1, 0, 1, 2, -1, -4]
sum = 0
print("input ===>", input)
print("Listing triplets adding to %d" % (sum))
result = find3Numbers(input, sum)
print(result)
    