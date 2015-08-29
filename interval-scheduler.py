'''
Question: Given a list of meeting start and end times find #meetings that have conflict

Source: http://stackoverflow.com/questions/27449948/schedule-optimization-in-python-for-lists-of-lists-interval-scheduling

Notes:
#Interval scheduling optimization is a standard problem with a greedy algorithm
#The following greedy algorithm does find the optimal solution:
# 1. Select the interval, x, with the earliest finishing time.
# 2. Remove x, and all intervals intersecting x, from the set of candidate intervals.
# 3. Continue until the set of candidate intervals is empty.

Test case:
Input >>> [[0, 1], [1, 2], [2, 3], [2, 5]]
#meetings with no conflict =  3
#meetings with conflict =  1
'''

def answer(meetings):
    last_end = -1
    ans = 0
    for end,start in sorted( (end,start) for start,end in meetings ):
        if start >= last_end:
            last_end = end
            ans += 1
    return ans, (len(meetings) - ans)

input = [[0,1],[1,2],[2,3],[2,5]]
print("Input >>>", input)
x,y = answer(input)
print ("#meetings with no conflict = ", x)
print ("#meetings with conflict = ", y)