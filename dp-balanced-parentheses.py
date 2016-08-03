#Generate all possible N pairs of balanced parentheses


'''
OBSERVATION:
N = 1 , result = ()
N = 2 , result = () + () = N1 + () = (()), ()() 
'''

def deep_copy(s,d):
	for x in s:
		d.append(x)


def balancedParentheisVariations(N):
	result = [['(',')']] #N=1
	new    = ['(',')']   #add  new
	new_result = []
	count = 1
	while count < N:
		count += 1
		for r in result:
			for i in range(len(r)):
				t = r[0:i+1] + new + r[i+1:]
				if t not in new_result:
					new_result.append(t)
		#store values from prior computation
		del result[:]
		deep_copy(new_result,result)
		del new_result[:]
	return result

N=3
result = balancedParentheisVariations(N)
print("All possible pairs of balanced parentheses for N=%d" %(N))
for r in result:
	print("".join(r))

