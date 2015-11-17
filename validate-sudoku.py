'''
Determine if a Sudoko puzzle is valid

Sudoku Rules:
1. 9x9 grid
2. Numbers 1-9 appear once in each row
3. Numbers 1-9 appear once in each column
4. Numbers 1-9 appear once in each  3x3

Questions to ask:
1. Are there empty cells?
2. How are empty cells represented?
3. Is an empty cell invalid Sudoku?
'''
#Reference: http://www.programcreek.com/2014/05/leetcode-valid-sudoku-java/
def ValidateSudoku(table):
    #check rows for unique value
    
    #check cols for unique value
    
    
    #check 3x3 for unique value
    for block in range(9):
        row = int(block/3) * 3
        col = (block%3) * 3
        for i in range(row,row+3):
            for j in range(col,col+3):
                #print("[%d,%d]" %(i,j))
        #print("##########")
                

ValidateSudoku([])