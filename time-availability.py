#Given availability of two people and duration for a meeting. Find the next earliest availability?

#Solution 1: Naive
def findFirstAvailability(a,b,duration):
	result = []
	alen = len(a)
	blen = len(b)
	aindex = 0
	bindex = 0
	while aindex < alen and bindex < blen:
		astart,aend = a[aindex]
		bstart,bend = b[bindex]
		if bstart >= aend:
			aindex += 1
			continue
		elif bend <= astart:
			bindex += 1
			continue
		elif bstart <= astart and bend <= aend:
			if bend-astart >= duration:
				return ([astart,bend])
		elif bstart <= astart and bend >= aend:
			if aend - bstart >= duration:
				return([bstart,aend])
		elif bstart >= astart and bend <= aend:
			if bend - bstart >= duration:
				return([bstart,end])
		elif bstart >= astart and bend >= aend:
			if aend - bstart >= duration:
				return([bstart,aend])
		if bend > aend:
			aindex +=1
		else:
			bindex +=1
	return  result

#Solution 2: Elegant
#Time complexity: O(n)
def findFirstAvailability2(a,b,duration):
	result = []
	alen = len(a)
	blen = len(b)
	aindex = 0
	bindex = 0
	while aindex < alen and bindex < blen:
		astart,aend = a[aindex]
		bstart,bend = b[bindex]
		#condition1: next a - NO OVERLAP
		if bstart >= aend:
			aindex += 1
			continue
		#condition2: next b	- NO OVERLAP
		elif bend <= astart:
			bindex += 1
			continue
		#condition3: OVERLAP!!!
		else:
			#max of start time
			maxStart = max(astart,bstart)
			#min of end time
			minEnd = min(aend,bend)
			if minEnd - maxStart >= duration:
				return [maxStart,minEnd]
			#condition4: next a, since bend is >
			if bend > aend:
				aindex +=1
			#condition5: next b since aend is >
			else:
				bindex +=1
	return  result


#a = [[1470384000, 1470387600] , [1470391200,1470405600], [1470416400,1470423600]]
#b = [[1470373200,1470384000], [1470405600,1470420000]]
#duration = 30 * 60   #seconds

a = [[8,9], [10,14], [17,19]]
b = [[5,8], [14,22]]
print("person1 availability", a)
print("person2 availability", b)

duration = 1 #hour
#print(findFirstAvailability(a,b,duration))
print("ealiest availability for ", duration , " hour = ", findFirstAvailability2(a,b,duration))
