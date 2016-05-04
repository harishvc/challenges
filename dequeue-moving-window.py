'''
There is a sliding window of size w which is moving by one position from the very left 
of the array to the very right. Find the max value as the window moves
'''

'''
REFERENCE:
http://articles.leetcode.com/sliding-window-maximum

NOTES:
1. Use dequeue -> add and remove from both ends
    - Linked list is another option
2. Store index position of max values in the dequeue as you interate the list
   - values of index in dequeue is high --- low
3. For each new value
   - Pop from left all index positions outside (on the left) of the window
   - Pop from right all values less than new value
'''
import collections
def SlidingWindow(a,w):
	dq = collections.deque()
	#initial setup
	for i in range(0,w):
		while dq and a[dq[-1]] <= a[i]:
			dq.pop()
		dq.append(i)
	print(a[i-w+1:i+1],a[dq[0]])
	for i in range(w,len(a)):
		#i = where the window ends
		#step 1: pop from left all values outside the start of the window
		while dq and dq[0] <= i-w:
			dq.popleft()
		#step 2: pop from right all values less than or equal to the new value
		while dq and a[dq[-1]] <= a[i]:
			dq.pop()
		#step 3: Add the new value at the end
		dq.append(i)
		#assert: all values in the queue are in descending order!
		print(a[i-w+1:i+1],a[dq[0]])

a = [4, 3, 2, 2, 6, 2, 5, 1]
w = 3
print("input >>>", a, "window size=",w)
SlidingWindow(a,w) 