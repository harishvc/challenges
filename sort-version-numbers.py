#Question: Implement compare function for version numbers
# Example: 0.1 < 1.1 < 1.2 < 13.37

#1. Observation:
# 1.1 Version numbers have minimum of 1 period
# 1.2 Sort by splitting the version numbers by period
# 1.3 Since version numbers are numeric preceding zeros are ignored. Example 1.02 and 1.2 will be considered equal  
#2. Algorithm:
# 2.1 Split each version on .
# 2.2 Create a list for each version 
# 2.3 Sort the list in ascending order 
#3. Complexity: 
# 3.1 Time complexity: O(n) where n is the number of entries + O (n log n) for sort 
#4. Test cases: 
#['5.10', '3.001.1', '2.5.7', '0.1','0.20.0', '3.01.5', '0.0.11', '3.5.09' , '3.5.80']
#5. Proof:
#sorted versions: ['0.0.11', '0.1', '0.20.0', '2.5.7', '3.001.1', '3.01.5', '3.5.09', '3.5.80', '5.10']
#6. Code:

versions1 = ['5.10', '3.001.1', '2.5.7', '0.1','0.20.0', '3.01.5', '0.0.11', '3.5.09' , '3.5.80']
versions2 = ['5.10', '3.001.1', '2.5.7', '0.1','0.20.0', '3.01.5', '0.0.11', '3.5.09' , '3.5.80']

def MySort(self):
    x = map(int,self.split('.'))   #split on .  and create a new list with versions as integers
    return x

print "input:", versions1

#Solution 1:
versions1.sort(key=MySort)
print"solution 1"
print "sorted versions:", versions1

#Solution 2:
print"solution 2"
print "sorted versions:", sorted(versions2,key=lambda x: map(int, x.split('.')))
