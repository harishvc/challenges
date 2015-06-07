#Question: Find sum of all even numbers from 1 to 100
print reduce(lambda x,y:x+y,range(2,101,2))
