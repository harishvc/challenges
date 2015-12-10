'''
Question: Given an array of integers, write a functions that returns true if there is a 
triplet (a,b,c) that satisfies a^2 + b^2 = c^2

Exmaple: [1,2,4,5,-3] 4^2 + -3^2 = 5^2

'''

#Time complexity::O(n^3)
#Solution 1:
def Solution1(input,ilength):
    for i in range(0,ilength):
        for j in range(1,ilength):
            for k in range(0, ilength):
                if (i != j != k):  #ignore comparing values in same index positions
                    if (input[i]**2 + input[j]**2 == input[k]**2):
                        print ("Triplet:", input[i],input[j],input[k])
                        return True
    return False



#Reference:https://stackoverflow.com/questions/2032153/how-to-find-pythagorean-triplets-in-an-array-faster-than-on2/2032765#2032765
#Solution 2:
#Space complexity: O(n)
#Time complexity: O(n) + O(n logn) + O(n^2) ~ O(n^2)
def Solution2(input,ilength):
    squares = []
    #Step 1: store n^2 in list
    for i in range(0,len(input)):
        squares.append(input[i]**2)
    #Step 2: sort - reduce # of comparisons
    squares.sort()
    #Step 3:
    inputsize = len(squares)-1
    for i in range(inputsize,-1,-1):
        j = 1 #left to right
        k = inputsize #right to left
        while (j<= k):
            if (squares[j] + squares[k] > squares[i]):
                    k -= 1 #got left, find next small value
            elif (squares[j] + squares[k] < squares[i]):
                    j += 1 #got right, find next large value
            else: #match
                print("Triplet: ", squares[j],squares[k],squares[i])
                j += 1 #go left
                k -= 1 #go right
                return True
    return False
                
input = [2,4,5,-3,-2,1,6]
print("Triplet? ", Solution2(input,len(input)))
