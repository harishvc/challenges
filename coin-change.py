'''
Find total #ways to reach a total using given denominations
'''

#http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
#https://www.youtube.com/watch?v=_fgjrs570YE&index=35&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
#Time Complexity: O(ij)
def count(denomination,total):
    dcount = len(denomination)
    table = [[0 for x in range(total+1)] for x in range(dcount+1)]
    for x in range(1,dcount+1):
        table[x][0] = 1 #initialize
    for i in range(1,dcount+1):
        for j in range(1,total+1):
            #print("i=%d,j=%d" % (i,j))
            if (denomination[i-1] > j):
                table[i][j] = table[i-1][j] 
            else:
                table[i][j] = table[i-1][j] + table[i][j-denomination[i-1]]
    #PrintMatrix(table)
    return(table[dcount][total])


def PrintMatrix(Table):
    for row in range(0,len(Table)):
        for col in range(0,len(Table[row])):
            print("%d" % (Table[row][col]),end=" ")
        print("")
        
        
denominations = [10, 25, 50]
total = 100
print("Total #ways to reach total=%d using denominations=%s is %d" % (total,denominations,count(denominations,total)))