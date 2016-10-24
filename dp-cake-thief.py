#Given the weight and a value of cakes and a duffel bag with max capacity, find the max value that can be filled!
#https://www.interviewcake.com/question/python/cake-thief


def maxValue(cake_tuples,capacity):
	maxValueLookup = [0] * (capacity + 1)
	for current_capacity in range(1,capacity+1):
		max_value_for_current_capacity = 0
		for cake_weight,cake_profit in cake_tuples:
			if cake_weight <= current_capacity:   #bottom up!
				max_value_using_cake = cake_profit + maxValueLookup[current_capacity-cake_weight]
				max_value_for_current_capacity = max(max_value_for_current_capacity,max_value_using_cake)
		maxValueLookup[current_capacity] = max_value_for_current_capacity
	print(maxValueLookup)
	return maxValueLookup[capacity]

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

print("%s max value=%d" % (cake_tuples,maxValue(cake_tuples,capacity)))

