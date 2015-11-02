'''
Question: Given a list and sum. Find 3 numbers in the list that add up to the given sum.
'''

'''
Solution1: Brut-force
1. Run 3 loops to find sum
2. Time complexity: O(n^3)
'''

'''
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
    
input = [2, 3, -1, 1]
sum = 4
print("input ===>", input)
print("Triplets adding to %d = " % (sum),end="")
findNumbers(input, sum)

    