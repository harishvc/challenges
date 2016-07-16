#Find the largest rectangular area in a histogram

'''
NOTES/OBSERVATION
1. Store index positions in stack
2. Stack has increasing values
3. Ignore equal values (value at top of stack == new value)
4. Pop values from stack when new value is <  value at to of stack
    - find area with appropriate width
5. After completing iteration, start popping values from the stack and find area

Reference
1. http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
'''


def maxArea(a):
	values = [] #store index positions with increasing value
	size = 0
	area = 0
	for i in range(len(a)):
		#case 1: empty
		if size == 0:
			values.append(i)
			size += 1
		#case 2: new value > 
		elif a[values[-1]] < a[i]:
			values.append(i)
			size +=1
		#case 3: same value; continue	
		elif a[values[-1]] == a[i]:
			continue
		#case 4: new value < 
		else:
			assert a[values[-1]] > a[i], "logic error"
			while True:
				#start popping values
				height = values.pop()
				size -= 1
				width = i #default width
				if size > 0:
					#IMPORTANT: new width!
					width = i - values[-1] -1
				area = max(area, a[height]*width)
				#IMPORTANT: Handle empty stack
				if size == 0 or a[values[-1]] <= a[i]:
					break
			#IMPORTANT: Append new value		
			values.append(i)
			size +=1
	#IMPORTANT: pop rest of the stack - values are increasing!
	width = 0
	while values:
		width +=1
		height = values.pop()
	area = max(area, a[height]*width)
	return area	


values = [[2,4,2,1], [6, 2, 5, 4, 5, 2, 6], [3,2, 4, 6,8], [3,6,3,6,5,2]]
for a in values:
	print("%s max area=%d" % (a,maxArea(a)))
