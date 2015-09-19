'''
Question: Given a two dimensional matrix where rows and columns are sorted in increasing order. 
Design an efficient algorithm that decides whether a number X appears in A.
'''

rows = 5
cols = 5
count = 0 
#Initialize matrix with increasing values
def init():
    global count
    count += 1
    return count

def Search(Matrix,input):
    x,y = 0,cols-1  #Top right corner
    while (x >=0 and y >=0 and x < rows and y < cols):
        if ( input > Matrix[x][y]):
            #next row
            x += 1
        elif( input < Matrix[x][y]):
            #next col
            y -= 1
        elif(input == Matrix[x][y]):
            return True
    return False
    
        
Matrix = [[init() for x in range(cols)] for y in range(rows)]

print("Is %d there? %s" % (10,Search(Matrix,10)))
print("Is %d there? %s" % (50,Search(Matrix,50)))
