#Find longest file path

#https://leetcode.com/problems/longest-absolute-file-path/
#https://discuss.leetcode.com/topic/55097/simple-python-solution


def lengthLongestPath(a):
	max_size = 0
	size_so_far = 0
	mystack = []
	myhash = {}
	for line in a.splitlines():
		name = line.lstrip('\t')
		size = len(name) 
		if "." not in name:
			size += 1  #file names don't end in \
		depth = len(line) - len(name)
		if depth == 0 :
			mystack.append(depth)
			myhash[depth] = size
			size_so_far = size
			max_size = size
		elif depth > mystack[-1]:
			mystack.append(depth)
			myhash[depth] = size
			size_so_far += size
		else:
			while len(mystack) > 0 and mystack[-1] >= depth:
				depth = mystack.pop()
				size_so_far -= myhash[depth]
			mystack.append(depth)
			myhash[depth] = size
			size_so_far += size
		#file
		if "." in name:
			max_size = max(max_size,size_so_far)
	#print(myhash, mystack)
	return max_size



input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print("Length of the longest file=",lengthLongestPath(input))
