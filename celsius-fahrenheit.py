#Question: Convert Celsius to Farenheit
#C = (F-32)*5/9
#F = (C*9)/5 + 32
Celsius = [29.5, 35.5, 37.3, 41.8]
Fahrenheit = map(lambda x: round(float (x*9/5) + 32, 2) , Celsius)
print Celsius
print Fahrenheit
