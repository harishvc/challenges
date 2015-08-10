'''
Question: Given stock prices during a time period find the maximum gain that can be made 
from one purchase followed by one sale of the stock
'''

'''
Reference: 
  1. http://stackoverflow.com/questions/7086464/maximum-single-sell-profit
  2. http://keithschwarz.com/interesting/code/?dir=single-sell-profit
Observation: Keep track of minimum price and gain
Time Complexity: O(n)
Space Conplexity: O(1) #constant
Output: 
[5, 10, 4, 6, 7] ->>>> Buy=5 Sell=10 Gain=5
[5, 10, 4, 6, 12] ->>>> Buy=4 Sell=12 Gain=8
[1, 2, 3, 4, 5] ->>>> Buy=1 Sell=5 Gain=4
'''

inputs = [
		  [5,10,4,6,7],
		  [5,10,4,6,12],
		  [1,2,3,4,5]
		 ]


for input in inputs:
	gain = 0
	min = input[0]
	buy = input[0]  #optional
	sell = input[0] #optional
	for buyPrice in input:
		#Condition 1
		if ( (buyPrice > min) and (buyPrice - min > gain)):
			gain = buyPrice - min  # new gain 
			sell = buyPrice  #sell price (optional)
			buy = min        #buy price  (optional)
		#Condition 2	
		elif (buyPrice < min):
			min = buyPrice #new min
	print("%s ->>>> Buy=%d Sell=%d Gain=%d" % (input,buy,sell,gain))
