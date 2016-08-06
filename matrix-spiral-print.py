#Print Spiral Matrix 

'''
OBSERVATION:
1. Spiral print starts at index 0,0
2. Direction = go right > got down > go left > go top
3. Have 4 pointers to indicate the start index in each direction 
'''

a = [[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

rows = len(a)
cols = len(a[0])

topR = 0           #index to start row
bottomR = rows-1   #index to start bottom row
leftC = 0          #index to start left col 
rightC = cols-1    #index to start right col

while topR < bottomR and leftC < rightC:
	#top row , left to right
	for i in range(leftC,rightC+1):
		print(a[topR][i],end=" ")
	topR +=1

	#far right col, top to bottom
	for i in range(topR,bottomR+1):
		print(a[i][rightC],end=" ")
	rightC -= 1

	#bottom row, right to left
	#IMPORTANT: -1 , going right to left
	for i in range(rightC,leftC-1,-1):
		print(a[bottomR][i],end=" ")
	bottomR -=1

	#left col, bottom to top
	#IMPORTANT: -1, going from bottom to top
	for i in range(bottomR,topR-1,-1):
		print(a[i][leftC],end=" ")
	leftC +=1

print()
#1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
