'''
Question: Given a two dimensional matrix print inside out (spiral order)
'''


def PrintMatrix(Table):
    for row in range(0,len(Table)):
        for col in range(0,len(Table[row])):
            print("%d" % (Table[row][col]),end=" ")
        print("")


#References
#1. http://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
#2. http://stackoverflow.com/questions/726756/print-two-dimensional-array-in-spiral-order
def SpiralBind(rowEnd,colEnd,table):
    rowStart = 0
    colStart = 0
    result = []
    while (rowStart < rowEnd and colStart < colEnd):
        #top row
        for i in range(colStart,colEnd):
            result.append(table[rowStart][i])
        rowStart +=1
        #right most col
        for i in range(rowStart,rowEnd):
            result.append(table[i][rowEnd-1])
        colEnd -=1
        #last row
        if(rowStart < rowEnd):
            for i in range(colStart,colEnd)[::-1]:
                result.append(table[rowEnd-1][i])
            rowEnd -=1
        #left most col
        if(colStart < colEnd):
            for i in range(rowStart,rowEnd)[::-1]:
                result.append(table[i][colStart])
            colStart += 1
    return result
        
        


table = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print("2x2 matrix")
PrintMatrix(table)
   
result = SpiralBind(4,4,table)
print("\nspiral bind ...")
print(result)
answer = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
assert result == answer, "invalid!!!!"