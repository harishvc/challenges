#Find all substrings
#A substring is a prefix or suffix of a string
#There are n^2 substring!

a = "banana"
result = set()
for i in range(len(a)):
	result.add(a[i:i+1])
	for j in range (i+1,len(a)):
		result.add(a[i:j+1])

print("All substrings for input >>> ", a)
z = sorted(result,key=len)
for x in z:
	print(x)