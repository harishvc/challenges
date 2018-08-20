'''
Question: Given stock prices during a time period find the maximum gain that can be made 
from one purchase followed by one sale of the stock

Reference: 
  1. http://stackoverflow.com/questions/7086464/maximum-single-sell-profit
  2. http://keithschwarz.com/interesting/code/?dir=single-sell-profit
  3. http://www.ideserve.co.in/learn/buy-and-sell-stock-part-one
'''


#Solution 1:
'''
Run two loops to find max profit
Time complexity: O(n^2)
'''

#Solution 2: Use queue
'''
Keep track of the increasing subsequence in a queue
If new value is greater than last seen value
   - add to queue,
   - calculate new profit, check if max profit
If new value is less than last seen value
    - pop all the values from queue
    - add the value to queue
In the end subtract the first and last values from queue to find profit, check if max profit
Time Complexity: O(n)
Space Complexity: O(n)
'''

#Solution 3: Modified solution #2, using two pointers
'''
Modify solution 2 to keeping track of lowest price and profit (no need for queue)
1. if new value is < lowest value
    - update new lowest value
2. if new value is > lowest value
    - update profit
Time Complexity: O(n)
Space Complexity: O(1)
'''
def maxProfit(a):
	profit = 0
	lowest_stock_price = a[0]
	for i in range(1, len(a)):
		if a[i] > lowest_stock_price:
			profit = max(profit,a[i] - lowest_stock_price)
		else:
			lowest_stock_price = a[i]  #new lowest!
	return profit 


stock_prices = [[5,10,4,6,7,2,7], [5, 10, 4, 6, 12],[1,2,3,4,5], [1,6,5]]
for s in stock_prices:
	print("input >>> %s  max profit=%d" % (s,maxProfit(s)))
