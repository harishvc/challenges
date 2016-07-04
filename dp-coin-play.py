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
'''


#Solution 1: recursive
def MaxValue(values,start,end):
	if start > end:
		return 0
	#IMPORTANT: Min since each player leaves the minimum value	
	t1 = min(MaxValue(values, start+2, end), MaxValue(values, start+1, end-1))
	t2 = min(MaxValue(values, start+1, end-1), MaxValue(values, start,  end-2))
	#option 1: pick start
	path1 = values[start] + t1
	#option 2: pick end
	path2 = values[end] + t2
	return (max(path1,path2))


#Solution 2: Dynamic Programming
def MaxValueDP(values,size):
	table = [[0 for x in range(size)] for y in range(size)]
	#Initialize for length=1
	for start in range(size):
		table[start][start] = values[start]
	#Generate values for length=2,3 ....	
	for l in range(2,size+1):
		#start value range 0  & 1
		for start in range(size-2):
			#end values changes based on start and length(l)
			#size =2  -> [0,1] [1,2],[2,3]
			#size =3  -> [0,2], [1,3]
			end = start + l - 1
			#IMPORTANT: break!
			if end == size:
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

