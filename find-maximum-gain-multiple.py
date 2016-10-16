'''
Question: Given stock prices during a time period find the maximum gain that can be made 
from one purchase followed by one sale of the stock **multiple times** without overlap

Reference: 
  1. http://www.ideserve.co.in/learn/buy-and-sell-stocks-part-two
'''

'''
NOTES:
1. Find increasing pairs to find profit
2. Sell and buy again

[100,80,120,130,70,60,100,125]

buy   sell 	 profit
80     120    40
120    130    10
60     100    40
100    125    25    

total profit = 115

'''

def maxProfit(a):
	max_profit = 0
	for i in range(1, len(a)):
		if a[i] > a [i-1]:
			max_profit += a[i] - a[i-1]
	return max_profit

stock_prices = [[100, 80, 120, 130, 70, 60, 100, 125]]
for s in stock_prices:
	print("input >>> %s  max profit=%d" % (s,maxProfit(s)))
