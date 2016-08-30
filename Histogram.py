#Find the largest rectangular area in a histogram

'''
NOTES/OBSERVATION
1. Store index positions in stack
2. Stack has increasing values
3. If we arrive at a bar with height greater than top of stack, 
   this may be the START of a max area rectangle so add to stack 
4. If we arrive at a bar with height smaller stack top, close ALL pending sub problems. 
   Calculate area at each bar - height is the popped element height 
   and width is how much we have traversed from the previous smaller 
   height that's why we store index in the stack 
5. At the end  calculate areas for all remaining sub problems

Reference
1. http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
2. https://prismoskills.appspot.com/lessons/Arrays/Largest_rectangle_under_histogram.jsp

'''


def findnewArea(mystack,mystack_size,height,i):
	left_boundry = 0
	right_boundry = 0
	area = 0
	#Find left & right boundry
	if mystack_size == 0:
		left_boundry = 0
		right_boundry = i
	else:
		left_boundry = mystack[-1]
		right_boundry = i -1
	area = (right_boundry - left_boundry) * height
	#print("area @ %d =%d  lb=%d rb=%d" % (height,area,left_boundry,right_boundry))
	return area


def maxArea(a):
	mystack = []
	mystack_size = 0 #initialize
	mystack.append(0) #initialize
	mystack_size +=1
	area = 0
	for i in range(1,len(a)):
		if a[i] > a[mystack[-1]]:
			mystack.append(i)
			mystack_size +=1
			#print(">>> mystack", mystack)
		else:
			#pop all values >= new value - including equal values
			while mystack_size > 0 and a[mystack[-1]] >= a[i]: 
				iheight = mystack.pop()
				mystack_size -= 1
				new_area = findnewArea(mystack,mystack_size,a[iheight],i)
				#Update new area
				area = max(area,new_area)
			mystack.append(i)
			mystack_size +=1
	#IMPORTANT: pop rest of the stack - values are increasing!
	width = 0
	while mystack:
		height = mystack.pop()
		width +=1 ##values greater than a[height]!
		new_area = a[height]*width 
		#print("area @ %d =%d" % (a[height],new_area))
		area = max(area, new_area)

	return area	


#values = [[2,4,2,1], [6, 2, 5, 4, 5, 2, 6], [3,2, 4, 6,8], [3,6,3,6,5,2], [10, 40, 30, 70, 10, 30, 60]]
values = [[10, 40, 30, 70, 10, 30, 60]]
for a in values:
	print("%s max area=%d" % (a,maxArea(a)))
