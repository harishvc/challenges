'''
Question: Given stock prices during a time period find the maximum gain that can be made 
from one purchase followed by one sale of the stock

Reference: 
  1. http://stackoverflow.com/questions/7086464/maximum-single-sell-profit
  2. http://keithschwarz.com/interesting/code/?dir=single-sell-profit

Observation:
Each data point we need to make a decision - buy or sell?
1. Time to Sell? 
   a. New data point > buy
   b. Profit from new data point is > profit
       b1. profit = sell-buy
       b2. profit = sell-maybebuy  
2. Time to buy?
   a. if new data point is < buy, perhaps "maybebuy" since we don't know about the following data points    

Complexity:
Time Complexity: O(n) , Space Complexity: O(1) 

Output: 
[5, 10, 4, 6, 7] ->>>> Buy=5 Sell=10 Gain=5
[5, 10, 4, 6, 12] ->>>> Buy=4 Sell=12 Gain=8
[1, 2, 3, 4, 5] ->>>> Buy=1 Sell=5 Gain=4

Dynamic Programming: (Bottom-up)
Start with the first value of the input and keep building the solution for higher values
'''

input = [5,10,4,6,7,2,7]
#input = [1,2,3,4,5]
#input = [5,1]

buy = input[0]
sell = None
profit = None
maybenewbuy = None

for x in range(1,len(input)):
	#Scenario 1: Sell
	if(input[x] > buy or (profit is not None and profit < input[x]-buy) or (maybenewbuy is not None and profit < input[x]-maybenewbuy)):
		sell = input[x]
		if (maybenewbuy is not None):
			buy = maybenewbuy
			maybenewbuy = None
		profit = sell - buy
	#Scenario 2: Buy
	elif(input[x] < buy):
		maybenewbuy = input[x]
print("Buy=%d Sell=%d Profit=%d" % (buy,sell,profit))
