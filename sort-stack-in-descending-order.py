'''
Question: Design an algorithm to sort a stack in descending order

Reference: http://www.quora.com/How-can-we-sort-a-stack-recursively-using-O-1-space

Algorithm: 
1. Compare last two elements
2. Add largest of the two elements back in the stack 
3. Continue  (recursive function call)
4. Add smallest back
5. At the end of each iteration, nth largest element is found (n is the #iteration)

Time complexity: O(n^2)
'''

def rec_sort(stack,i):
        if len(stack) <= i :
                return stack
        else:
                t1 = stack.pop()
                t2 = stack.pop()
                top = max(t1, t2)
                bot = min(t1, t2)
                #Push max back in stack (descending order)
                stack.append(top)  
                rec_sort(stack,i)
                #Push min at end!
                stack.append(bot)

if __name__ == '__main__':
        a = [6,3,7,2,9,3, 10, 19, 0]
        print("input >>>", a)
        for i in range (1,len(a)+1):
            rec_sort(a,i)
        print("output >>>", a)