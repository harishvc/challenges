'''
How many different 10-digit numbers can be formed starting from 1? 
The constraint is that the movement from 1 digit to the next is similar to the movement of the Knight in a chess game.

Reference: http://stackoverflow.com/questions/2893470/generate-10-digit-number-using-a-phone-keypad
'''

def initialize():
	table = [[0 for i in range(3)] for j in range(4)]
	values = [1,2,3,4,5,6,7,8,9,None,0,None]
	rows = len(table)
	cols = len(table[0])
	count = 0
	for i in range(rows):
		for j in range(cols):
			table[i][j] = values[count]
			count += 1
	return table

#given value find coordinates 
def getCoordinates(value,table):
	rows = len(table)
	cols = len(table[0])
	for i in range(rows):
		for j in range(cols):
			if table[i][j] == value:
				return([i,j])

#Next Knights move from current coordinates
def nextKnightMove(value,table):
	i, j = getCoordinates(value,table)
	rows = len(table)
	cols = len(table[0])
	result = []
	#down 3 right
	if(i+1 < rows and j+2 < cols and table[i+1][j+2] is not None):
		result.append(table[i+1][j+2])
	#down 3 left
	if(i+1 < rows and j-2 >= 0 and table[i+1][j-2] is not None):
		result.append(table[i+1][j-2])
	#up 3 right
	if(i-1 >= 0 and j+2 < cols and table[i-1][j+2] is not None):
		result.append(table[i-1][j+2])
	#up 3 left
	if(i-1 >= 0 and j-2 >= 0 and table[i-1][j-2] is not None):
		result.append(table[i-1][j-2])
	#down 1 right
	if(i+2 < rows and j+1 < cols and table[i+2][j+1] is not None):
		result.append(table[i+2][j+1])
	#down 1 left
	if(i+2 < rows and j-1 >= 0 and table[i+2][j-1] is not None):
		result.append(table[i+2][j-1])
	#up 1 right
	if(i-2 >= 0 and j+1 < cols and table[i-2][j+1] is not None):
		result.append(table[i-2][j+1])
	#up 1 left
	if(i-2 >=0  and j-1 >= 0 and table[i-2][j-1] is not None):
		result.append(table[i-2][j-1])
	return result

#http://stackoverflow.com/questions/2893470/generate-10-digit-number-using-a-phone-keypad
def generateTableM(table,mtable,digits,start):
	if digits == 1:
		return 1
	if (mtable[digits][start] == 0):
		for next in nextKnightMove(start,table):
			mtable[digits][start] += generateTableM(table,mtable,digits-1,next)
	#else:
		#print("found ...",digits,start)
	return mtable[digits][start]


table = initialize()
#memoization table
mtable = [[0 for i in range(10)] for j in range(11)]
print(generateTableM(table,mtable,10,1)) #mtable[10][1]	= 1424
