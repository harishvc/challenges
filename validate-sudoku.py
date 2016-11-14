#Determine if a Sudoko puzzle is valid
#https://leetcode.com/problems/valid-sudoku/

'''
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


'''
NOTES

Inspiration: 
https://discuss.leetcode.com/topic/59807/python-short-code-with-explanation-with-small-space-used/3

LOGIC:
Store tuples in a set to keep track of visited values
Reduces time complexity to nxn with additional storage (depending on values present)
'''

def ValidateSudoku(table):
    rows = len(table)
    cols = len(table[0])
    visited = set()
    for i in range(0,rows):
        for j in range(0,cols):
            if table[i][j] == "."
                continue
            else:
                num = table[i][j]
                #case 1: unique in row
                if(("row",i,num) in res):
                    return False
                else:
                    res.add(("row",i,num))
                #case 2: unique in col
                if(("col",j,num) in res):
                    return False
                else:
                    res.add(("col",j,num))
                #case 3: unique in 3x3
                if((i//3,j//3,num) in res):
                    return False
                else:
                    res.add((i//3,j//3,num))
    return True

ValidateSudoku([])