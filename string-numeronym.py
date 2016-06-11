#Generate all Numeronyms for a given string
#Example: "careercup"=>"c7p","ca6p","c6up","car5p","ca5up","care4p"...

def generateNumeronyms(a):
	size = len(a)
	S = 1 #start characters are fixed
	E = 1 #end characters are fixed
	N = size-S-E #max 
	result = set()
	for n in range(N,0,-1):
		#print("aaa",n)
		#FRONT
		for front in range(0,size):
			count = front + S + E + n
			if (count == size):
				print("%s%d%s" % (a[0:front+1],n,a[size-1]))
			elif (count < size):
				print("%s%d%s" % (a[0:front+1],n,a[count-1:]))
			else:
				break

a ="careercup"
generateNumeronyms(a)

'''
c7p
c6up
ca6p
c5cup
ca5up
car5p
c4rcup
ca4cup
car4up
care4p
c3ercup
ca3rcup
car3cup
care3up
caree3p
c2eercup
ca2ercup
car2rcup
care2cup
caree2up
career2p
c1reercup
ca1eercup
car1ercup
care1rcup
caree1cup
career1up
careerc1p
'''

















