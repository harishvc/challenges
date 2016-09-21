#Determine the maximum possible value from the coin play game

'''
DETAILED PROBLEM:
Consider a row of n coins of values v1 . . . vn, where n is even. 
We play a game against an opponent by alternating turns. 
In each turn, a player selects either the first or last coin from the row, 
removes it from the row permanently, and receives the value of the coin. 
Determine the maximum possible amount of money we can definitely win if we move first.
'''

'''
Example 1:  8, 15, 3, 7
player1: 7, 15 
player2: 8, 3

OBSERVATION:
1. The user (player1) starts first
2. The user (player1) can pick the start or end value
3. The players leaves the other player with minimum value

REFERENCE:
1. http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
2. https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/NPotGold.java
3. http://stackoverflow.com/questions/22195300/understanding-solution-to-finding-optimal-strategy-for-game-involving-picking-po
4. http://ideone.com/ug1DOx
5. https://github.com/harishvc/challenges/blob/master/images/dp-game-play.jpg
'''


#Solution 1: recursive
def MaxScore(a,start,end):
	#IMPORTANT: exit condition, start > end (not start == end)
	if start > end:
		return 0
	else:
		#Each player leaves the minimum value
		path1 = a[start] + min(MaxScore(a,start+2,end), MaxScore(a,start+1,end-1))
		path2 = a[end]   + min(MaxScore(a,start+1,end-1), MaxScore(a,start,end-2))
		return max(path1,path2)

#Solution 2: recursive with path
def MaxScoreP(a,start,end,path):
	#IMPORTANT: exit condition
	if start > end:
		return 0,path
	else:
		#1st branch
		path1Value,path1Path = MaxScoreP(a,start+2,end,path+[a[start]])
		path2Value,path2Path = MaxScoreP(a,start+1,end-1,path+[a[start]])
		if path1Value < path2Value:
			b1v,b1p = a[start]+path1Value,path1Path
		else:
			b1v,b1p = a[start]+path2Value,path2Path


		#2nd branch	
		path3Value,path3Path = MaxScoreP(a,start+1,end-1,path+[a[end]])
		path4Value,path4Path = MaxScoreP(a,start,end-2,path+[a[end]])
		if path3Value < path4Value:
			b2v,b2p = a[end]+path3Value,path3Path
		else:
			b2v,b2p = a[end]+path4Value,path4Path

		#return max of branch1, baranch2
		if b1v >  b2v:
			return b1v,b1p
		else:
			return b2v,b2p


#Solution 3: Dynamic Programming
def MaxValueDP(values,size):
	table = [[0 for x in range(size)] for y in range(size)]
	#Initialize for length=1
	for start in range(size):
		table[start][start] = values[start]
	#Generate values for length=2,3 ....
	#size+1 to include all values!	
	for l in range(2,size+1):
		#start value range 0  & 1
		for start in range(0,size):
			#end values changes based on start and length(l)
			#size =2  -> [0,1] [1,2],[2,3]
			#size =3  -> [0,2], [1,3]
			end = start + l - 1
			#IMPORTANT: break when start or end index is not valid
			if start >= size or start+1 >= size or start+2 >= size or end >= size:
				break
			#option 1: pick start	
			path1 = values[start] + min(table[start+2][end],table[start+1][end-1])
			#option 2: pick end
			path2 = values[end] + min(table[start+1][end-1],table[start][end-2])
			table[start][end] = max(path1,path2)
	#print(table)
	return table[0][size-1]



a = [3,9,1,2]

#Solution 1: recursive
#print(MaxValue(a,0,len(a)-1))

#Solution 2: DP
player1 = MaxValueDP(a,len(a))
print("values >>>", a)
print("player1=%d" % (player1))

