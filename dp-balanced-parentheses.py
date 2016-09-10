#Generate all possible N pairs of balanced parentheses


'''
OBSERVATION:

N = 0 , result = None
N = 1 , result = ()
N = 2 , result = () + () = N1 + () = (()), ()() 

1. New values are generated from prior value

'''

def findVariations(n):
	base = ['(',')']
	result = [['(',')']]
	for i in range(2, n+1):
		new_result = []
		for r in result:
			new_result += [r[:p+1]+base+r[p+1:] for p in range(0,len(r))]
		result = new_result
	return result


n = 3
print("Variations of balanced parenthesis when n =%d" % (n))
for r in findVariations(n):
	print("".join(r))
