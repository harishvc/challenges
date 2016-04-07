'''
Given a list of intervals merge overlapping intervals
Example: [1,3][4,6][2,9]   ===> [1,9]
'''

def mySort(self):
	return self[0]

def mergeTimeIntervals(a):
	result = []
	endTimeQueue = []
	endTimeCount = 0
	endTimeCurrent = 0 #current time interval
	#step 1: sort by start time 
	a.sort(key=mySort)
	#step 2: compare end time of first value with start time of second value
	for time in a:
		start,end = time[0],time[1]
		if endTimeCount == 0:
			endTimeQueue.append(time)
			endTimeCount += 1
		elif start <= endTimeQueue[endTimeCurrent][1]:
			#merge time
			endTimeQueue[endTimeCurrent][1] = end
		else:
			#new time
			endTimeQueue.append(time)
			endTimeCurrent +=1
			endTimeCount +=1
	return endTimeQueue


a = [[1,3],[9,12],[4,8],[3,5]]
print("time intervals >>> ", a)
print("merged intervals >>> ", mergeTimeIntervals(a))
