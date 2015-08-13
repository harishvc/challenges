#Question: Design an algorithm to sort a stack in descending order
#http://www.quora.com/How-can-we-sort-a-stack-recursively-using-O-1-space

#Time complexity: O(n^2)
def rec_sortD(stack):
        if len(stack) <= 1 :
                return stack
        else:
                t1 = stack.pop()
                t2 = stack.pop()
                top = max(t1, t2)
                bot = min(t1, t2)
                #Ascencding order
                #stack.append(bot)
                #rec_sort(stack)
                #stack.append(top)
                #Descending order
                stack.append(top)
                rec_sortD(stack)
                stack.append(bot)

if __name__ == '__main__':
        #a = [6,3,7,2,9,3, 10, 19, 0]
        a = [7,2,3,5]
        rec_sortD(a)
        print(a)