
#Source: http://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python


# Creates a list containing 5 lists initialized to 0
#[[0 for x in range(cols_count)] for x in range(rows_count)]
Matrix = [[0 for x in range(5)] for x in range(5)] 

Matrix[0][0] = 3
Matrix[4][0] = 2

print (Matrix[0][0]) # prints 1
print (Matrix[4][0]) # prints 5
print(Matrix)

#sort
#Source: http://stackoverflow.com/questions/2173797/how-to-sort-2d-array-by-row-in-python
from operator import itemgetter
Matrix2 = sorted(Matrix, key=itemgetter(1))
print(Matrix2)
