'''
Question: Merge K sorted list of size N 
'''

#http://stackoverflow.com/questions/19474924/merging-k-sorted-lists-using-priority-queue
import heapq
def addtoheap(h, i, it):
    try:
        heapq.heappush(h, (next(it), i))
    except StopIteration:
        pass

def mergek(*lists):
    its = list(map(iter, lists))
    h = []
    for i, it in enumerate(its):
        addtoheap(h, i, it)
    while h:
        v, i = heapq.heappop(h)
        addtoheap(h, i, its[i])
        yield v

for x in mergek([1, 3, 5], [2, 4, 6], [7, 8, 9], [10,11,12]):
    print(x)

